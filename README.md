## flask-azure-demo

Demo web app tobe deploy on Azure Kubernetes

### Deployment history

In Azure, deploy project using _Deployment center (preview)_

* Authorize with GitHUB
* Select project
** Auto create in project files: `.github/workflows`, `manifests`
* Update _manifests files_ to correct service port, also changing `ingress.yml` api level to `networking.k8s.io/v1`

### Deployment notes

* To export direct to internet: `kubectl expose deployment <service-name> --type=LoadBalancer --port 80 --target-port 8080`
