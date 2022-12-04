# Module 10 - Homework
we'll deploy Credit Card prediction model from the homework 5.

## Description
tensorflow serving(C++), with focus on inference

## Getting Started

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing
```
docker build -t hw-10:v001 .
docker run -it --rm -p 9696:9696 hw-10:v001 
python test.py 

kubectl apply -f hw-10-deploy.yaml


kind create cluster
kubectl get service
kubectl get pod


```