#! /usr/bin/env python
# coding: utf-8

import logging
import sys


import gspread_sheet_servise as gs_service
import twitter_service as twi_service

import config

from error import ResponseHasError

# for GCP entry point
def handle_cloud_functions(event, context):
    try:
        gspread_service = gs_service.GSpreadSheetService()
        record = gspread_service.choose_record()

        twitter_service = twi_service.TwitterService(endpoint=config.TWITTER_POST_ENDPOINT)
        result = twitter_service.tweet(record)
        logging.info("Tweet Success")

        gspread_service.write_timestamp(result)
        logging.info("Write created_at")

    except ResponseHasError as e:
        logging.warning(e.args[0])
        sys.exit()

if __name__ == "__main__":
    sys.dont_write_bytecode = True
    handle_cloud_functions(event=None, context=None)
