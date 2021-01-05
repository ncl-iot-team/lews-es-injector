FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["python", "es_ingest.py"]