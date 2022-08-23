## flask-azure-demo

Demo web app tobe deploy on Azure Kubernetes

### Deployment notes

* Export to internet: `kubectl expose deployment <service-name> --type=LoadBalancer --port 80 --target-port 8080`
