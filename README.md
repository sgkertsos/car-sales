This is the final project for the DataTalks Club Data Engineering Zoomcamp 2024.

In this project we will display used car sales in the United States.

**Dataset**  

We will use the Vehicles Sales dataset from Kaggle. The dataset can be found in the URL below:  

https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data  

as a zip file.

The file can also be found in the data folder.

**Moving the data to a bucket**
 - Create a GCP bucket 
 
 For this we will use terraform which must be installed on our computer. Then we have to modify the main.tf file located in the terraform folder. We are going to make the following changes:

    1. For the provider
        a. Replace the project ID with your GCP project ID
        b. Replace the region with your GCP region
    2. For the bucket
        a. Replace name with your bucket name
        b. Replace the bucket location with your bucket location

We also have to copy our service account json file to the keys directory or paste the contents of our json file to the tf_service_account.json file. 

NOTE:
The service account can be created with the following roles:
    Storage Admin
    BigQuery Admin
    Compute Admin
    
Then from the terraform directory we execute:

    terraform init
    terraform plan
    terraform apply

    Type yes and hit Enter.

The bucket is created in our GCP storage.

- Run Mage
Used instructions from mage.ai website:

https://docs.mage.ai/getting-started/setup

For this you must have git and Docker installed. Then you run the following commands:

cd mage 
cp dev.env .env 
rm dev.env 
docker-compose up

Forward port 6789 on your local machine.

Then you can access Mage by typing:

http://localhost:6789

in your browser.
