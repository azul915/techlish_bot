FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /app

RUN set -ex && \
    apk --no-cache add python3-dev

COPY ./app/requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python", "main.py"]
