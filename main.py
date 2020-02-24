# coding: utf-8

import logging
import sys
from datetime import datetime, timedelta, timezone

import gspread_sheet
import twitter
from error import ResponseHasError

row_num_content = gspread_sheet.get_row_num_and_formatted_content()

# def execute():
# for GCP entry point
def execute(event, context):
    try:
        result_dict = twitter.tweet(row_num_content)
        logging.info("Tweet Success")

        gspread_sheet.write_timestamp(result_dict)
        logging.info("Write created_at")

    except ResponseHasError as e:
        logging.warning(e.args[0])
        sys.exit()

#execute()