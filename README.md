# vncc-kubernetes

The aim of this project is to develop a simple web application for retrieving informations from a database, according to specific criteria expressed by the user, throughout a simple HTML page. The principal technology used for this purpose is Kubernetes, which allows to orchestrate container in an efficient way.   
The application is characterised by 3 pods, which developed 3 different services:
- MySQL database: database for mantain data;
- client interface: web interface for the user to express filtering criteria for the data in the database;
- API REST: retrieve data from the database and deliver them to the user.

## Technologies
- Flask
- MySQL
- HTML
- CSS
- Javascript

## Usage
In this project there are also some script to deploy the application in a simplier way:
- ```start.sh```: allow to create the images, the pods and expose the services on the relative ports;
- ```stop.sh```: close the application deleting all the pods in running.
