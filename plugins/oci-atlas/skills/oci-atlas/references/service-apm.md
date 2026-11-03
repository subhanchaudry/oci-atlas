# Application Performance Monitoring and traces

Reviewed: 2026-11-03

## Choose the application signal

APM helps inspect application transactions, spans and related performance signals. Infrastructure metrics answer a different question. Use traces to locate time spent across application dependencies; use synthetic monitoring for a selected client journey from its configured vantage point.

## Prerequisites and boundaries

Select the APM domain, supported agent/tracer, application runtime and ingestion endpoint. Identify management IAM separately from ingestion keys and client instrumentation. Browser-visible keys and private server ingestion credentials have different exposure expectations. Never put private keys into frontend code.

## Working sequence

1. Choose one meaningful request path and an application/service naming convention.
2. Configure the supported agent or OpenTelemetry integration, endpoint and credentials through runtime configuration.
3. Preserve trace propagation across supported HTTP/messaging boundaries. Redact credentials, personal data and sensitive SQL/request attributes.
4. Issue a bounded request and locate its trace. Inspect incomplete spans, sampling and clock/time-window mismatches before declaring a dependency absent.
5. Correlate slow spans with application logs and database/runtime metrics. A long database span is a starting observation, not proof the database needs scaling.
6. For synthetic monitoring, select the real network vantage point and credential handling, then inspect the actual journey result.

## Operate

Budget ingestion volume, retention and synthetic execution using the selected service terms. Sampling changes what is visible. Record instrumentation version and service names with application releases so dashboards do not silently track obsolete labels.

Before removing a domain, key or monitor, enumerate dependent emitters and incident workflows. Use [observability delivery](recipe-observability-delivery.md) for alerts and [Logging](service-logging-audit-connectors.md) for retained evidence.

## Sources

- [APM documentation](https://docs.oracle.com/en-us/iaas/application-performance-monitoring/home.htm)
- [Microservice tracing architecture](https://docs.oracle.com/en/solutions/oci-apm-for-microservices/)
