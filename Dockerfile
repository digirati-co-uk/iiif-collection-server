FROM python:3-alpine

RUN apk add python3-dev build-base linux-headers pcre-dev uwsgi-python3

EXPOSE 8000

WORKDIR /opt/iiif-collection-server

COPY ./app/requirements.txt /opt/iiif-collection-server/
COPY ./app/*.py /opt/iiif-collection-server/

RUN pip install -r requirements.txt

CMD ["gunicorn","--log-level", "debug", "-w", "2", "-k", "uvicorn.workers.UvicornWorker", "-b", " 0.0.0.0:8000", "iiif-collection-server:app"]
