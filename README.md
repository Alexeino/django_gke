# Django App Deployment on GKE Cluster

<mark> &nbsp; Branch &nbsp; </mark> &rarr; &nbsp; **gke_integration_03**
-   

<mark> &nbsp; Features &nbsp; </mark> 
-
-   App Run on GKE with CloudSQL (GCLOUD) as Database
-   Use a side car cloud-sql container to connect to cloudSQL instance on Gcloud.
-   Ready to Run Yaml configs
-   Gunicorn is used as worker for django app

<mark> &nbsp; Docker Image &nbsp; </mark> &rarr; alexeino/django_gke:0.4
-

<mark> &nbsp; To Run App over GKE Cluster &nbsp; </mark>
-
*   Create a CloudSQL PostgreSQL Instance on Gcloud and note 
    -   Instance name
    -   Instance password
*   Create a Database and note
    -   Database name
*   Create a User and note
    -   Database user
    -   User Password
    -   <mark> Will be used inside django settings </mark>
*   Create a Service Account and Download it's credentials JSON file
    -   Service Account Name
    -   Download JSON credentials file
    -   <mark> will be used to connect App container and CloudSQL side car container to Cloudsql instance

*   Create a Secret to store Service Account credentials JSON file 

    <mark> Replace your credentials json file path </mark>
```
kubectl create secret generic cloudsql-oauth-credentials \
--from-file=credentials.json=<path_to_json>/<file.json>
```
-    This will create a secret and store JSON file inside a secret, This secret will be used by side-car cloud-sql container to open connection to cloudsql through command. For that this file will be mounted to volume to cloud-sql container.

*   Modify sample_secret.yaml by replacing following fields by original values after encoding
    -   SECRET_KEY: <your_secret_key_encoded>
    -   DEBUG: <your_debug_value_encoded>
    -   DATABASE_NAME: <your_database_name_encoded> &nbsp; &rarr; *Cloudsql Database Name*
    -   DATABASE_USER: <your_database_user_encoded> &nbsp; &rarr; *Cloudsql Database User Name*
    -   DATABASE_PASSWORD: <your_database_password_encoded> &nbsp; &rarr; *Cloudsql User Password*
    -   &nbsp; <mark> To encode see below command for example &nbsp;</mark>
    -   ```
        echo -n "my_db_name" | base64
        echo -n "my_db_password" | base64
        ```
        *Use -n to avoid newlines or spaces**

* After modifying secret, Apply all resources on your cluster (Assuming you connected to your GKE cluster)
    -   ```kubectl apply -f k8s/```

#### You should have your Django App running over GKE. Login to mycontainer on the pod and try running *makemigrations* and *migrate* to check if App is successfully connected to CloudSQL Instance.
#### Try accessing your app on service Load Balancer IP.

### Important Commands
-   To Authenticate or login to gcloud through terminal  
    ```gcloud auth application-default login```
-   To see cloudsql instance connection string  
    ```gcloud sql instances describe <INSTANCE_NAME> --format="valueconnectionName)"```
-   Creating a Secret to store Service Account JSON file to mount on clodu-sql side container  
    ```kubectl create secret generic cloudsql-oauth-credentials --from-file=credentials.json=/home/alexeino/Documents/Gcloud/django_gke/gcloud_service_account.json```
-   To see cloudsql instance  
    ```gcloud sql instances list```