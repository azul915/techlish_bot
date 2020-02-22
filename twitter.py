# coding: utf-8

import datetime
import json
import logging
import os
import subprocess
import time
from typing import Dict

import pytz
from requests_oauthlib import OAuth1Session

import config
import cred
from error import ResponseHasError

CK = cred.CONSUMER_KEY
CS = cred.CONSUMER_SECRET
AT = cred.ACCESS_TOKEN
ATS = cred.ACCESS_TOKEN_SECRET

TIMEZONE = config.TIMEZONE
FORMAT = config.FORMAT

def jst(created_at):
    """
    """
    st = time.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y')
    utc_time = datetime.datetime(st.tm_year, st.tm_mon,st.tm_mday, \
        st.tm_hour,st.tm_min,st.tm_sec, tzinfo=datetime.timezone.utc)
    jst_time = utc_time.astimezone(pytz.timezone(TIMEZONE))
    str_time = jst_time.strftime(FORMAT)
    return str_time

# from main.py
def tweet(rn_c) -> Dict[str, str]:
    """
    TwitterAPIでツイートを実行する

    Args:

    Returns:
        dict: Return
    """

    twitter = OAuth1Session(CK, CS, AT, ATS)

    url = config.TWITTER_POST_ENDPOINT

    params = {"status" : rn_c['formatted_content']}

    res = twitter.post(url, params = params)
    res_dict = json.loads(res.text)

    if res.status_code != 200:

        err_message = res_dict['errors'][0]['message']
        raise ResponseHasError(err_message)

    else:
        created_at = res_dict['created_at']
        jst_created_at = jst(created_at)

        return { 'status_code': res.status_code, 'created_at': jst_created_at, 'row_num': rn_c['row_num'] }
