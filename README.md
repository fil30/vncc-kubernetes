# vncc-kubernetes

The purpose of this project is to develop a simple web application for retrieving informations from a database, according to specific criteria inserted by the user, throughout a simple HTML page. The principal technology used is Kubernetes, which allows to deploy the application efficiently.   
The application is composed by three pods, which develope three different services:
- MySQL database: database to store data;
- Web interface: allow the user to interact with the data contained in the database;
- Database API: expose the data in the database in a JSON format.

## Technologies
- Flask
- MySQL
- HTML
- CSS
- Javascript
- SQLAlchemy

## Usage
In this project there are also two scripts to deploy the application:
- ```start.bat```: the script file which starts the appplication deploying all the pods;
- ```stop.bat```: the script file which closes the application deleting all the running pods.
