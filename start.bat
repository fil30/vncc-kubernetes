# Build new images

docker build -t mysql-db ./src/mysql-db
docker build -t db-con ./src/db-con
docker build -t app-image ./src/web-app

# Create a container registry to keep all the images 

docker run -d -p 4000:5000 --restart=always --name registry registry:2

#  Create a new tag for an image

docker tag mysql-db localhost:4000/mysql-db
docker tag db-con localhost:4000/db-con
docker tag app-image localhost:4000/app-image

# Push the images on the local registry

docker push localhost:4000/mysql-db
docker push localhost:4000/db-con
docker push localhost:4000/app-image

# Define all the yaml files to deploy the application

kubectl apply -f yaml-file/mysql-pvc.yml
kubectl apply -f yaml-file/mysql-deployment.yml
kubectl apply -f yaml-file/db-con-deployment.yml
kubectl apply -f yaml-file/web-app-deployment.yml

# Sleep command

timeout /t 8

# Port forwarding

kubectl port-forward service/web-app 5000:5000