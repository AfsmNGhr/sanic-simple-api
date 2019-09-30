FROM python:3.7.4-alpine3.10

COPY requirements.txt /

RUN apk --update add --no-cache --virtual .base build-base && \
    pip install --no-cache-dir -r /requirements.txt && \
    adduser -D -S -u 1000 -G users -h /home/sanic-simple-api sanic-simple-api && \
    apk del .base && \
    rm -rf /tmp/* /var/tmp/* /usr/share/man /tmp/* /var/tmp/* \
        /var/cache/apk/* /var/log/* ~/.cache

COPY . /home/sanic-simple-api
RUN rm /home/sanic-simple-api/requirements.txt && \
    chown -R sanic-simple-api:users /home/sanic-simple-api

USER sanic-simple-api
WORKDIR /home/sanic-simple-api
CMD python app.py
