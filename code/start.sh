#!/bin/bash

# Create the new images
docker build -t mysql-db ./db
docker build -t api-db ./api-db
docker build -t app-image ./webapp

# Create a container registry on port 5000 to keep all the images 
docker run -d -p 4000:5000 --restart=always --name registry registry:2

docker tag mysql-db localhost:4000/mysql-db
docker tag api-db localhost:4000/api-db
docker tag app-image localhost:4000/app-image

# Push the images on the local registry
docker push localhost:4000/mysql-db
docker push localhost:4000/api-db
docker push localhost:4000/app-image

# Apply all the YAML to deploy yhe application
kubectl apply -f yaml-file/mysql-pv.yml
kubectl apply -f yaml-file/mysql-deployment.yml
kubectl apply -f yaml-file/api-db-deployment.yml
kubectl apply -f yaml-file/webapp-deployment.yml

# Port forwarding

kubectl port-forward service/api-db 5000:5000

kubectl port-forward service/webapp 5001:5001