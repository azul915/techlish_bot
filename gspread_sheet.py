# coding: utf-8

import logging
import random
from typing import Dict

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import config
import cred


def sheet():
    """
    初期処理をして、使用するシートを取得する。
    """

    scope = [config.FEEDS, config.GOOGLE_DRIVE]

    credential_info = {
                "type": config.SERVICE_ACCOUNT,
                "project_id": cred.SHEET_PROJECT_ID,
                "private_key_id": cred.SHEET_PRIVATE_KEY_ID,
                "private_key": cred.SHEET_PRIVATE_KEY,
                "client_email": cred.SHEET_CLIENT_EMAIL,
                "client_id": cred.SHEET_CLIENT_ID,
                "auth_uri": config.AUTH_URI,
                "token_uri": config.TOKEN_URI,
                "auth_provider_x509_cert_url": config.AUTH_PROVIDER_X509_CERT_URL,
                "client_x509_cert_url": cred.SHEET_CLIENT_X509_CERT_URL
    }

    credentials = ServiceAccountCredentials.from_json_keyfile_dict(credential_info, scope)
    gc = gspread.authorize(credentials)
    wks = gc.open(config.TECHLISH_SPREAD_SHEET).sheet1

    return wks


def choose(wks) -> Dict[str, str]:
    """
    SpreadSheetに登録されている単語をランダムで取得する。

    Args:

    Returns:
        dict: Return any rows
    """

    # A行に値がない場合、実行を止める
    if len(wks.col_values(1)) == 0:
        logging.critical('The spreadsheet has no value in A columns.')

    rows = wks.get_all_values()
    idx = random.randint(0, len(rows)-1)

    row_obj = rows[idx]
    row_num = idx + 1

    return {'r': row_num,'w': row_obj[0], 'c': row_obj[1], 'm': row_obj[2], 'a': row_obj[3]}


def formatting(d: Dict[str, str]) -> str:
    """
    tweetを成形して返す。補足が続く場合、改行する。 

    Args:
        arg1 (dict[str, str]): First argument
            key_pattern
                r : int 列番号
                w : str 英単語
                c : str 品詞のカテゴリー
                m : str 日本語での意味
                a : str 補足
    Returns:
        str or None: Return tweet_content

    Raises:
        ValueError: if arg1 is empty string.
    """

    formatted_content = '''\
{word}({category}): {mean}
{any}
#SoftwareEnglish
\
'''.format(word=d['w'], category=d['c'], mean=d['m'], any=d['a'])

    return { 'row_num': d['r'], 'formatted_content': formatted_content}


# from main.py
def get_row_num_and_formatted_content():

    wks = sheet()
    choosen = choose(wks)
    return formatting(choosen)

# from main.py
def write_timestamp(result_dict):

    wks = sheet()
    row_str = str(result_dict['row_num'])

    wks.update_acell("E"+row_str, result_dict['created_at'])
