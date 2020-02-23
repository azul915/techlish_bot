FROM python:3.8-alpine

WORKDIR /app

RUN set -ex && \
    apk update  && \
    apk add python3-dev

COPY main.py .
COPY config.py .
COPY cred.py .
COPY gspread_sheet.py .
COPY twitter.py .
COPY error.py .
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD [ "python", "main.py" ]
