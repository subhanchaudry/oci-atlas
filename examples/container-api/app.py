"""Private OCI application: process health and a bounded SQL dependency check."""
import base64
import json
import os


def check_database():
    import oci
    import oracledb

    # The runtime receives a resource principal; no user key is baked into the image.
    signer = oci.auth.signers.get_resource_principals_signer()
    client = oci.secrets.SecretsClient({}, signer=signer, timeout=(5, 15))
    bundle = client.get_secret_bundle(
        os.environ['ATLAS_DB_SECRET_ID'], stage='CURRENT',
        retry_strategy=oci.retry.NoneRetryStrategy(),
    ).data
    credentials = json.loads(base64.b64decode(
        bundle.secret_bundle_content.content, validate=True).decode('utf-8'))
    if set(credentials) != {'username', 'password'}:
        raise ValueError('The database secret must contain username and password')
    dsn = os.environ['ATLAS_DB_DSN']
    if not dsn.lower().startswith('tcps://'):
        raise ValueError('Use a TCPS Easy Connect descriptor')
    with oracledb.connect(
        user=credentials['username'], password=credentials['password'], dsn=dsn,
        ssl_server_dn_match=True, tcp_connect_timeout=10, retry_count=0,
    ) as connection:
        connection.call_timeout = 10000
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1 FROM dual')
            if cursor.fetchone() != (1,):
                raise RuntimeError('Unexpected database response')
    return {'database': 'reachable'}


def create_app(database_check=check_database):
    def application(environ, start_response):
        path = environ.get('PATH_INFO', '/')
        if environ.get('REQUEST_METHOD') != 'GET':
            status, payload = '405 Method Not Allowed', {'error': 'method_not_allowed'}
        elif path == '/health':
            status, payload = '200 OK', {'status': 'ok'}
        elif path == '/db-check':
            try:
                payload, status = database_check(), '200 OK'
            except Exception:
                # Driver/service errors can contain connection metadata. Keep them out of responses.
                status, payload = '503 Service Unavailable', {'error': 'database_unavailable'}
        else:
            status, payload = '404 Not Found', {'error': 'not_found'}
        body = json.dumps(payload).encode('utf-8')
        start_response(status, [('Content-Type', 'application/json'),
                                ('Content-Length', str(len(body))),
                                ('Cache-Control', 'no-store')])
        return [body]
    return application


app = create_app()
