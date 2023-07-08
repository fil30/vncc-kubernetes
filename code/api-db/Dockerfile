# Creazione di un Dockerfile che definisce un'immagine per il servizio db_api.

FROM python:3.9

WORKDIR /project

COPY ./ .

COPY  requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "data-api.py"]