#! /usr/bin/env python
# coding: utf-8

import datetime
import json

import time
import pytz
from requests_oauthlib import OAuth1Session

import record as rec
import tweet
import config
import settings

class TwitterService:
    def __init__(self, client={}, endpoint=""):
        self.client = OAuth1Session(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
        self.endpoint = endpoint

    def tweet(self, record):
        t = tweet.Tweet(record)
        if settings.DEBUG == "true":
            print("debug mode")
            return

        res = self.client.post(self.endpoint, params = t.content)

        res_dict = json.loads(res.text)
        print(json.dumps(res_dict, indent=2))
        created_at = res_dict['created_at']
        print(created_at)
        st = time.strptime(created_at, config.TWITTER_FORMAT)
        utc_time = datetime.datetime(st.tm_year, st.tm_mon,st.tm_mday, \
            st.tm_hour,st.tm_min,st.tm_sec, tzinfo=datetime.timezone.utc)
        jst_time = utc_time.astimezone(pytz.timezone(config.TIMEZONE))
        jst_str = jst_time.strftime(config.FORMAT)
        return rec.Record(num=record.num, word=record.word, category=record.category, mean=record.mean, supplement=record.supplement, created_at=jst_str)
