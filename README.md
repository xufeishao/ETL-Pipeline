# ETL-Pipeline

## Description
Extract-Transform-Load tasks.
- Extracts transactional data of 400k invoices from redshift
- Transforms the data by identifying and removing duplicates
- Loads the transformed data to an s3 bucket

## Requirements
- Docker for Mac: Docker >= 20.10.2, installation refer to https://docs.docker.com/desktop/install/mac-install/ 
- Docker for Windows: installation refer to https://docs.docker.com/desktop/install/windows-install/
- Python 3.8 and above

## How to run the code
- Copy the .env.example file to .env and fill out the environment varibles.

- Make sure you are executing the code from the etl_pipeline folder and you have Docker Desktop running.

- To run it locally first build the image.

  #### docker image build -t etl-pipeline:0.1 .
  
  #### docker image build -t etl-pipeline:0.1 .

Then run the etl job using docker:

  #### docker run --env-file .env etl-pipeline:0.1
