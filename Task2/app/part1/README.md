* Start kuber
```sh
minikube start --driver=docker
minikube addons enable metrics-server
kubectl apply -f ./kubernetes
minukube service scaletestapp
```
* Check state commands
```sh
kubectl get pods
kubectl get nodes
kubectl get services
kubectl logs scaletestapp
```
* Delete everything
```sh
kubectl delete all --all
```

* Locust is better to launch with sth like this:
```sh
locust -f .\locustfile.py --host http://127.0.0.1:54884
```