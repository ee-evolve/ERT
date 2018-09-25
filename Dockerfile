FROM python:3.7.0-alpine3.8 as builder

LABEL maintaner="EvolvE <evolve@equalexperts.com>"

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

COPY updater.py updater.py

RUN python -m unittest discover tests

CMD [ "python", "./updater.py" ]
