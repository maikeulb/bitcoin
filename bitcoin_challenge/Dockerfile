FROM python:3.6-alpine

COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY bitcoin_challenge.py config.py entrypoint.sh ./

RUN chmod +x ./entrypoint.sh

ENV FLASK_APP bitcoin_challenge.py
ENV FLASK_APP_CONFIG=config.ProductionConfig

EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]
