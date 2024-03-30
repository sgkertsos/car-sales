from google.cloud import bigquery
from google.cloud.exceptions import NotFound

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

def create_partitioned_table():

    client = bigquery.Client()

    table_id = '<Your Dataset ID>.car_sales'

    schema = [
        bigquery.SchemaField("year", "INTEGER"),
        bigquery.SchemaField("make", "STRING"),
        bigquery.SchemaField("model", "STRING"),
        bigquery.SchemaField("trim", "STRING"),
        bigquery.SchemaField("body", "STRING"),
        bigquery.SchemaField("transmission", "STRING"),
        bigquery.SchemaField("vin", "STRING"),
        bigquery.SchemaField("state", "STRING"),
        bigquery.SchemaField("condition", "INTEGER"),
        bigquery.SchemaField("odometer", "INTEGER"),
        bigquery.SchemaField("color", "STRING"),
        bigquery.SchemaField("interior", "STRING"),
        bigquery.SchemaField("seller", "STRING"),
        bigquery.SchemaField("mmr", "INTEGER"),
        bigquery.SchemaField("sellingprice", "INTEGER"),
        bigquery.SchemaField("saledate", "TIMESTAMP"),
    ]

    table = bigquery.Table(table_id, schema=schema)
    table.time_partitioning = bigquery.TimePartitioning(field="saledate")

    try:
        client.get_table(table_id)
        print("Table already exists.")
    except NotFound:
        table = client.create_table(table)  # Make an API request.
        print("Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id))

@data_exporter
def export_data(data, *args, **kwargs):
    create_partitioned_table()
    return data
