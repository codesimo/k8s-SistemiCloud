# Sample 3-Layer Application in Kubernetes

This repository contains a simple 3-layer application deployed in Kubernetes, using Flask for the frontend and backend layers, and PostgreSQL for the database layer.

## Prerequisites

Before running the application, ensure you have the following installed:

1. Docker: To build the container images.
2. Kubernetes: To deploy the application using the provided example.yaml file.
3. kubectl: The Kubernetes command-line tool to interact with the Kubernetes cluster.

## Getting Started

1. Clone this repository:

```bash
git clone https://github.com/codesimo/k8s-SistemiCloud.git
cd k8s-SistemiCloud
```

2. Build the Docker images for the frontend and backend layers:

```bash
docker build -t myfrontend:latest ./frontend
docker build -t mybackend:latest ./backend
```

3. Deploy the application to your Kubernetes cluster:

```bash
kubectl apply -f example.yaml
```

The example.yaml file contains Kubernetes deployment and service configurations for the frontend, backend, and PostgreSQL database layers.

4. Accessing the Application

Once the application is successfully deployed, you can access it through the Kubernetes services.

- Frontend: Access the Flask frontend by navigating to `http://<frontend-service-ip>` in your web browser.
- Backend: The backend is accessed internally by the frontend service to handle data processing. It is not directly exposed externally.
- PostgreSQL: The PostgreSQL database is not directly accessible from outside the cluster. The backend service interacts with it internally.

## Cleaning Up

To remove the application and associated resources from your Kubernetes cluster, run the following command:

```bash
kubectl delete -f example.yaml
```

## `run.sh`

Alternatively, you can use the provided `run.sh` script, which automates the build and deployment process. Ensure the script has execution permission:

```bash
chmod +x run.sh
```

Then, you can run the application with a single command:

```bash
./run.sh
```

## Customization

You can customize the application by modifying the Flask frontend and backend code in their respective directories. Additionally, you can adjust the example.yaml file to accommodate specific deployment requirements.
