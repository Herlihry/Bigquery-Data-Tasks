# 1. Set up a project in the Google Cloud Platform and enable the BigQuery and Google Sheets API.
# 2. Install the required libraries:
#    pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pandas gspread gspread_dataframe

# 3. Authenticate your script to access the API using a service account key file or by using OAuth 2.0.
from google.oauth2.credentials import Credentials

creds = Credentials.from_service_account_file("service_account_key.json")

# 4. Use the `bigquery` library to run a query and store the results in a Pandas DataFrame.
from google.cloud import bigquery
import pandas as pd

# Construct a BigQuery client object.
client = bigquery.Client()

# Set up the query.
query = """
    SELECT *
    FROM `bigquery-public-data.samples.natality`
    WHERE year > 2000
    LIMIT 1000
"""

# Run the query and store the results in a DataFrame.
df = client.query(query).to_dataframe()

# 5. Use the `gspread` library to authenticate and access the Google Sheets API.
import gspread

# Authenticate using the service account key file.
client = gspread.authorize(creds)

# 6. Use the `gspread` library to create a new Google Sheet or open an existing one.
# Create a new Google Sheet.
sheet = client.create("My Sheet")

# Or open an existing Google Sheet.
sheet = client.open("My Sheet")

# 7. Use the `gspread_dataframe` library to export the DataFrame to the Google Sheet.
import gspread_dataframe as gd

# Export the DataFrame to the Google Sheet.
gd.set_with_dataframe(sheet.worksheet("Sheet1"), df)
