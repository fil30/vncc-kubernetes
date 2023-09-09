# Create a Dockerfile to retrieve data from the database

FROM python:3.9

WORKDIR /Carapp

COPY ./db-con.py ./db-con.py

COPY  requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "db-con.py"]