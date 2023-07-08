# Create a Dockerfile for Python

FROM python:3.9

WORKDIR /project

COPY ./ .

COPY  requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "web-app.py"]