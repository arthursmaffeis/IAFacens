FROM python:3.9-slim

RUN pip install mlflow==2.6.0 psycopg2-binary boto3 pymysql

WORKDIR /mlflow

EXPOSE 3000

CMD mlflow server \
    --backend-store-uri postgresql://mlflow:mlflow@postgres:5432/mlflow \
    --default-artifact-root s3://mlflow \
    --host 0.0.0.0 \
    --port 3000