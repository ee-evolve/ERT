FROM python:3.7.0-alpine3.8 as builder

LABEL maintaner="EvolvE <evolve@equalexperts.com>"

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY updater.py updater.py

CMD [ "python", "./updater.py" ]
