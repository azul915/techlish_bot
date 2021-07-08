#! /usr/bin/env python
# coding: utf-8

import random
import record as rec

import settings
import logging

import gspread_sheet_adaptor as gs_adaptor

class GSpreadSheetService:
    def __init__(self, adaptor={}):
        self.adaptor = gs_adaptor.GSpreadSheetAdapter()

    def choose_record(self):
        records = self.adaptor.get_all_values()
        logging.info("got all records")
        idx = random.randint(0, len(records)-1)

        str_num = str(idx + 1)
        logging.info(f'\"{records[idx][0]}\" was chosen')
        return rec.Record(\
                num=str_num,\
                word=records[idx][0],\
                category=records[idx][1],\
                mean=records[idx][2],\
                supplement=records[idx][3],\
                created_at=records[idx][4])

    def write_timestamp(self, result):
        if settings.DEBUG == "true":
            self.adaptor.write_timestamp_debug()
        else:
            self.adaptor.write_timestamp(result)
