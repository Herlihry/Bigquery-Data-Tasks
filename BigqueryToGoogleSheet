# Import the necessary libraries
import pandas as pd
from google.cloud import bigquery
from google.oauth2.credentials import Credentials

# Set your BigQuery project ID and dataset ID
project_id = 'your-project-id'
dataset_id = 'your-dataset-id'

# Set your Google Sheets ID and sheet name
sheets_id = 'your-sheets-id'
sheet_name = 'Sheet1'

# Authenticate your Google Cloud account
credentials = Credentials.from_service_account_file('path/to/service_account.json')

# Connect to BigQuery
client = bigquery.Client(project=project_id, credentials=credentials)

# Set the query string
query_string = 'SELECT * FROM `{}.{}`'.format(dataset_id, 'your-table-name')

# Query the data
query_job = client.query(query_string)
df = query_job.to_dataframe()

# Export the data to Google Sheets
service = build('sheets', 'v4', credentials=credentials)

# Clear the existing data in the sheet
sheet = service.spreadsheets().get(spreadsheetId=sheets_id).execute()
sheet_id = sheet['sheets'][0]['properties']['sheetId']
request = {
