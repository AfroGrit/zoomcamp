# Module 10 - Homework
we'll deploy Credit Card prediction model from the homework 5.

## Description
model serving(C++), with focus on inference

## Getting Started

* TODO

### Dependencies

* TODO

### Installing
```
docker build -t hw-10:v001 .
docker run -it --rm -p 9696:9696 hw-10:v001 
python test.py 

kubectl apply -f hw-10-deploy.yaml
```

### Autoscaling
```
kubectl autoscale deployment credit-card --name credit-card-hpa --cpu-percent=20 --min=1 --max=3
kubectl get hpa
kubectl get hpa credit-card-hpa --watch
```

### Quick utils
```
kind create cluster
kubectl get service
kubectl get pod
```