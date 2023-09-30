# Django App Deployment on GKE Cluster

<mark> &nbsp; Branch &nbsp; </mark> &rarr; &nbsp; **gke_integration_02**
-   

<mark> &nbsp; Features &nbsp; </mark> 
-
-   Simple Django App 
-   Runs over Gunicorn Workers
-   No DB attached uses db.sqlite3
-   Runs on GKE Cluster, Just apply k8s/ config via kubectl 

<mark> &nbsp; Docker Image &nbsp; </mark> &rarr; alexeino/django_gke:0.2
-
-   <mark> &nbsp; To Run Locally &nbsp; </mark> 
    -   Clone the Repo and cd into rep
    -   Build the image with  &nbsp;  ```docker build -t <image_name>:<image_tag>```
    -   Run image locally with following command
        -   ```docker run -it --rm -p 8000:8000 -e DEBUG=True -e SECRET_KEY=<your_secret_key> --name=<container_name> <image_name>:<image_tag>```

<mark> &nbsp; To Run App over GKE Cluster &nbsp; </mark>
-
*   Prepare Secrets by replacing your values in sample_secret.yaml make sure to encode with base64 like below
    -   ```echo "<your_original_secret_key> | base64```
    -   ```echo "<your_DEBUG_value> | base64```
*   Replace encoded values inside sample_secret.yaml
*   Apply all kubernetes resource yamls
    -   ```kubectl apply -f k8s/```
*   Deployment, Secret and Service(Load balancer) would be created on your cluster