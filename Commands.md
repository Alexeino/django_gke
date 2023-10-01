### Important Commands
-   To Authenticate or login to gcloud through terminal  
    ```gcloud auth application-default login```
-   To see cloudsql instance connection string  
    ```gcloud sql instances describe <INSTANCE_NAME> --format="valueconnectionName)"```
-   Creating a Secret to store Service Account JSON file to mount on clodu-sql side container  
    ```kubectl create secret generic cloudsql-oauth-credentials --from-file=credentials.json=/home/alexeino/Documents/Gcloud/django_gke/gcloud_service_account.json```
-   To see cloudsql instance  
    ```gcloud sql instances list```