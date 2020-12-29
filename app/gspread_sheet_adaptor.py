# coding: utf-8

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import config
import settings
import sys

class GSpreadSheetAdapter:
    def __init__(self, client={}):
        scope = [config.FEEDS, config.GOOGLE_DRIVE]
        info = {
                "type": config.SERVICE_ACCOUNT,
                "project_id": settings.SHEET_PROJECT_ID,
                "private_key_id": settings.SHEET_PRIVATE_KEY_ID,
                "private_key": settings.SHEET_PRIVATE_KEY.replace('\\n', '\n'),
                "client_email": settings.SHEET_CLIENT_EMAIL,
                "client_id": settings.SHEET_CLIENT_ID,
                "auth_uri": config.AUTH_URI,
                "token_uri": config.TOKEN_URI,
                "auth_provider_x509_cert_url": config.AUTH_PROVIDER_X509_CERT_URL,
                "client_x509_cert_url": settings.SHEET_CLIENT_X509_CERT_URL
        }
        creds = ServiceAccountCredentials.from_json_keyfile_dict(info, scope)
        gc = gspread.authorize(creds)
        sheet1_cli = gc.open(config.TECHLISH_SPREAD_SHEET).sheet1

        if len(sheet1_cli.col_values(1)) == 0:
            logging.critical('The spreadsheet has no value in A columns.')
        else:
            self.client = sheet1_cli

    def get_all_values(self):
        return self.client.get_all_values()

    def write_timestamp(self, result):
        self.client.update_acell("E"+result.num, result.created_at)
