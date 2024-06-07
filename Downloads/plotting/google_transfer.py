import pandas as pd 
import os
from googleapiclient.discovery import build 
from google.oauth2 import service_account
from google.auth.exceptions import TransportError


SCOPES=['https://www.googleapis.com/auth/drive']
service_account_file='service.json'
parent_folder_id='1g9pJ7rebjZcqAMhAolzhc9daLjXUwoFk'

def authenticate():
    creds=service_account.Credentials.from_service_account_file(service_account_file, scopes=SCOPES)
    return creds
def report_card(dataframe):
    #Create a binary yes or no for dm errors (specific dm errors)

    #Create some sort of localization error metric (maybe difference in encorder values)

    #Create Humidity metric for dms (could me a max humidity seen across all dms)

    #create humidity metric for Centerbody

    #Something to allow for additional files to be added (slack conversations, RC error codes)
    pass

def health_database(dataframe, str):
    #create a report to add to overall robotics health, this could be just a description of the dataframe with droped columns
    dataframe.describe().to_csv(f'{str}_health.csv')

def upload(file_path, str):
    creds=authenticate()
    service=build('drive', 'v3', credentials=creds)
    
    file_metadata={
        'name': str, 
        'parents': [parent_folder_id]
    }
    try: 
        file=service.files().create(
            body=file_metadata,
            media_body=file_path,
        ).execute()
        os.remove(f'{str}_health.csv')
        print("Done!!")

    except TimeoutError:
        print("Upload timed out, Retrying...")
        file=service.files().create(
            body=file_metadata,
            media_body=file_path,
        ).execute()
        os.remove(f'{str}_health.csv')
        print("Done!!")

    except TransportError:
        print("Connect to the wifi")

