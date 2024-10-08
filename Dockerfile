FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --progress-bar off --upgrade pip
RUN pip install --progress-bar off -r requirements.txt

CMD uvicorn fast_api_service:app --host 0.0.0.0 --port 8000
