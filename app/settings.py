import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

# twitter.py
SHEET_PROJECT_ID = os.environ['SHEET_PROJECT_ID']
SHEET_PRIVATE_KEY_ID = os.environ['SHEET_PRIVATE_KEY_ID']
SHEET_PRIVATE_KEY = os.environ['SHEET_PRIVATE_KEY']
SHEET_CLIENT_EMAIL = os.environ['SHEET_CLIENT_EMAIL']
SHEET_CLIENT_ID = os.environ['SHEET_CLIENT_ID']
SHEET_CLIENT_X509_CERT_URL = os.environ['SHEET_CLIENT_X509_CERT_URL']

# twitter.py
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']