# Remove all

kubectl delete -f yaml-file/mysql-deployment.yml
kubectl delete -f yaml-file/db-con-deployment.yml
kubectl delete -f yaml-file/web-app-deployment.yml
kubectl delete -f yaml-file/mysql-pvc.yml

# Remove the container registry

docker stop registry
docker rm registry