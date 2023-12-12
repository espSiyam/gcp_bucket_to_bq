import functions_framework
from google.cloud import bigquery
from google.cloud import storage

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def hello_gcs(cloud_event):
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    bucket_name = data["bucket"]
    file_name = data["name"]
    print(f"Processing file: {file_name} and bucket: {bucket_name}")

    # Set up BigQuery client
    bigquery_client = bigquery.Client()

    # Set up GCS client
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    print("Blob created")

    # Set up BigQuery job config
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=False,
        max_bad_records=1000,  
        schema=[
                bigquery.SchemaField("date", "DATETIME", mode="REQUIRED"),
                bigquery.SchemaField("website", "STRING", mode="REQUIRED"),
                bigquery.SchemaField("url", "STRING", mode="REQUIRED"),
                bigquery.SchemaField("title", "STRING", mode="REQUIRED"),
                bigquery.SchemaField("text", "STRING", mode="REQUIRED"),
                bigquery.SchemaField("translated_title", "STRING", mode="REQUIRED"),
                bigquery.SchemaField("translated_text", "STRING", mode="REQUIRED"),
                bigquery.SchemaField("category", "STRING", mode="REQUIRED"),
                bigquery.SchemaField("main_image", "STRING", mode="NULLABLE"),
            ]
    )
    print("Job config created")
    # Specify BigQuery dataset and table
    dataset_id = 'news_data'
    table_id = 'daily_news_bd'

    # Get the BigQuery dataset reference
    dataset_ref = bigquery_client.dataset(dataset_id)

    # Get the BigQuery table reference
    table_ref = dataset_ref.table(table_id)

    # Set the GCS URI as the data source for the BigQuery load job
    uri = f"gs://{bucket_name}/{file_name}"
    print("exporting data to BigQuery by uri : ", uri)

    # Load data into BigQuery
    load_job = bigquery_client.load_table_from_uri(
        uri,
        table_ref,
        job_config=job_config
    )

    load_job.result()  # Wait for the job to complete

    print(f"Data loaded from {uri} into BigQuery table {dataset_id}.{table_id}")