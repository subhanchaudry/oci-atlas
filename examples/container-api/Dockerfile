FROM python:3.12.12-slim-bookworm
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
USER 10001:10001
EXPOSE 8080
CMD ["uvicorn", "app:app", "--interface", "wsgi", "--host", "0.0.0.0", "--port", "8080", "--workers", "2"]
