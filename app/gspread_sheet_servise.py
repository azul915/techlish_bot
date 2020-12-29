# coding: utf-8

import random
import record as rec

import gspread_sheet_adaptor as gs_adaptor

class GSpreadSheetService:
    def __init__(self, adaptor={}):
        self.adaptor = gs_adaptor.GSpreadSheetAdapter()

    def choose_record(self):
        records = self.adaptor.get_all_values()
        idx = random.randint(0, len(records)-1)

        str_num = str(idx + 1)
        return rec.Record(\
                num=str_num,\
                word=records[idx][0],\
                category=records[idx][1],\
                mean=records[idx][2],\
                supplement=records[idx][3],\
                created_at=records[idx][4])

    def write_timestamp(self, result):
        self.adaptor.write_timestamp(result)
