This is the final project for the DataTalks Club Data Engineering Zoomcamp 2024.

In this project we will display used car sales in the United States.

First of all you have to clone this project by typing:

git clone https://github.com/dgkertsos/car-sales.git

**Dataset**  

We will use the Vehicles Sales dataset from Kaggle. The dataset can be found in the URL below:  

https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data  

as a zip file.

The file can also be found in the data folder.

**Create a GCP bucket and a BigQuery Dataset** 
The GCP bucket will be used to store the data from the car-prices.zip file in a partitioned parquet format. Then the data will be transferred to a BigQuery table with the help of Mage.

 For this we will use terraform which must be installed on our computer. Then we have to modify the main.tf file located in the terraform folder. We are going to make the following changes:

    1. For the provider
        a. Replace the project ID with your GCP project ID
        b. Replace the region with your GCP region
    2. For the bucket
        a. Replace name with your bucket name
        b. Replace the bucket location with your bucket location
    3. For the dataset
        a. Replace name with the dataset name
        b. Replace the project ID with your GCP project ID
        c. Replace the dataset location with your dataset location

We also have to paste the contents of our service account json file to the keys/tf_service_account.json file. 

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

The bucket is created in our GCP storage and the dataset will be created in our bigquery datasets.

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
