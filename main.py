import os
#from dotenv import load_dotenv
#load_dotenv()

from src.extract import extract_transactional_data
from src.transform import identify_and_remove_duplicated_data
from src.load_data_to_s3 import df_to_s3

dbname = os.getenv('dbname')
host = os.getenv('host')
port = os.getenv('port')
user = os.getenv('user')
password = os.getenv('password')
aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_access_key_id = os.getenv('aws_secret_access_key_id')
s3_bucket = 'waia-data-dump'
key = 'bootcamp2/etl/sxf_online_deduplicated.csv'


online_trans_cleaned = extract_transactional_data(dbname, host, port, user, password)
online_deduplicated = identify_and_remove_duplicated_data(online_trans_cleaned)
df_to_s3(online_deduplicated, key, s3_bucket, aws_access_key_id, aws_secret_access_key_id)