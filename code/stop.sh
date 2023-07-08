#!/bin/bash

# Remove all pods, deployments, services and the persistent volume
kubectl delete -f yaml-file/mysql-deployment.yml
kubectl delete -f yaml-file/api-db-deployment.yml
kubectl delete -f yaml-file/webapp-deployment.yml
kubectl delete -f yaml-file/mysql-pv.yml

# Remove the container registry
docker stop registry
docker rm registry