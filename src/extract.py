import psycopg2
import pandas as pd
import boto3
from io import StringIO


def connect_to_redshift(dbname, host, port, user, password):
    """Method that connects to redshift. This gives a warning so will look for another solution"""

    connect = psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )

    print("connection to redshift made")

    return connect


def extract_transactional_data(dbname, host, port, user, password):
    # connect to read_shift
    connect = connect_to_redshift(dbname, host, port, user, password)
    # add the query
    query = '''
 SELECT ot.invoice, 
        ot.stock_code,
        ot.quantity,
        CAST(invoice_date As DateTime) AS invoice_date,
        ot.price,
        ot.price * ot.quantity as total_order_value,
        ot.customer_id,
        ot.country,
       CASE WHEN s.description IS NULL THEN 'Unknown'
            ELSE s.description END AS description
FROM bootcamp.online_transactions ot
LEFT JOIN ( SELECT *
            FROM bootcamp.stock_description
            WHERE description <> '?') AS s
ON ot.stock_code = s.stock_code
WHERE ot.customer_id <> ''
AND ot.stock_code NOT IN ('BANK CHARGES', 'POST', 'D', 'M', 'CRUK')'''
    online_trans_cleaned = pd.read_sql(query, connect)

    print('The shape of the extracted and transformed data is: ', online_trans_cleaned.shape)
    return online_trans_cleaned
