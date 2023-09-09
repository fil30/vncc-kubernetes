# Create a Dockerfile for the web page

FROM python:3.9

WORKDIR /Carapp

COPY ./static/style-sheet.css ./static/style-sheet.css

COPY ./templates/web-page.html ./templates/web-page.html

COPY ./web-app.py ./web-app.py

COPY  requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "web-app.py"]