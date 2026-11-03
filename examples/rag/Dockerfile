FROM python:3.12.12-slim-bookworm
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY rag.py schema.sql ./
USER 10001:10001
ENTRYPOINT ["python", "rag.py"]
CMD ["--help"]
