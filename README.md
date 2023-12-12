# Cloud Function for GCP - Data Transfer from Cloud Storage to BigQuery

This Google Cloud Function is designed to be triggered by changes in a Cloud Storage bucket. Upon triggering, it transfers data from the specified bucket to a BigQuery table.

## Prerequisites

Before deploying and using this function, make sure you have the following in place:

- [Google Cloud Platform (GCP) project](https://cloud.google.com/resource-manager/docs/creating-managing-projects)
- [Google Cloud Storage bucket](https://cloud.google.com/storage/docs/creating-buckets)
- [Google BigQuery dataset and table](https://cloud.google.com/bigquery/docs/tables)

## Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Install Dependencies**

    Ensure you have Python 3.x installed. Install the required Python packages using the following:

    ```bash
    pip install -r requirements.txt
    ```

    This installs the necessary dependencies, including the `functions-framework`, `google-cloud-bigquery`, and `google-cloud-storage` packages.

3. **Configuration**

    Update the `requirements.txt` file and replace the placeholder values in the code with your actual GCP project details, dataset, and table information.

4. **Deploy the Cloud Function**

    Deploy the Cloud Function to GCP using the following command:

    ```bash
    gcloud functions deploy hello_gcs \
      --runtime python310 \
      --trigger-resource YOUR_BUCKET_NAME \
      --trigger-event google.storage.object.finalize
    ```

    Replace `YOUR_BUCKET_NAME` with the name of your Cloud Storage bucket.

5. **Testing**

    Upload a file to the specified Cloud Storage bucket and observe the logs to ensure that the function is triggered and the data is loaded into BigQuery successfully.

## Function Details

- **Function Name:** `hello_gcs`
- **Trigger:** Cloud Storage bucket changes (`google.storage.object.finalize`)
- **Dependencies:**
  - `functions-framework` version 3.*
  - `google-cloud-bigquery`
  - `google-cloud-storage`


Feel free to reach out if you have any questions or need further assistance.
