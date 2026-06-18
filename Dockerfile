FROM python:3.13-slim
LABEL authors="Matvey"

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV BASE_URL=http://host.docker.internal:8000

COPY . .

CMD ["pytest"]
