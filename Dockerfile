FROM python:3-alpine

RUN apk add python3-dev build-base linux-headers pcre-dev uwsgi uwsgi-python3

ENV COLLECTION_SERVER_S3_BUCKET placeholder
ENV COLLECTION_SERVER_S3_BASE_PREFIX placeholder
ENV COLLECTION_SERVER_S3_ACCESS_KEY placeholder
ENV COLLECTION_SERVER_S3_SECRET_KEY placeholder
EXPOSE 5000

WORKDIR /opt/iiif-collection-server

COPY ./app/requirements.txt /opt/iiif-collection-server/
COPY ./app/*.py /opt/iiif-collection-server/

ENV FLASK_APP collection_server.py

RUN printenv && pip install -r requirements.txt

CMD ["gunicorn","--log-level", "debug", "-w", "2", "-b", " 0.0.0.0:5000", "collection_server:app"]
