# ETL-Pipeline

## Description
- Extracts transactional data of 400k invoices from redshift
- Transforms the data by identifying and removing duplicates
- Loads the transformed data to an s3 bucket


- src/extract.py: a function script to extract data from redshift and create a dataframe excluding 'description' with
  '?' and 'BANK CHARGES', 'POST', 'D', 'M', 'CRUK', and fill 'NULL' with 'Unknown'
- src/transform.py: a function script to identify and remove duplicates
- src/load_data_to_s3.py: a function script to load the transformed data to s3 bucket

## Requirements
- Docker for Mac: Docker >= 20.10.2, installation refer to https://docs.docker.com/desktop/install/mac-install/
- Docker for Windows: 
  - Installation refer to https://docs.docker.com/desktop/install/windows-install/
  - Manual installation steps for older WSL version: Docker WSL 2

## How to run the code
- Make sure your Docker Desktop running
- Copy the .env.example file to .env and fill out the environment variables.

- To run it locally first build the image.

  #### docker image build -t etl-pipeline:0.1 .


- Then run the etl job using docker:

  #### docker run --env-file .env etl-pipeline:0.1
