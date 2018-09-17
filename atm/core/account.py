#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 0019 下午 21:17
# @Author  : xiaoyafei
# @Site    : 
# @File    : account.py
# @Software: PyCharm

from core import db_handler

def load_current_balance(account_id):
    db_api = db_handler.db_handler()
    data = db_api('select * from accounts where account=%s'% account_id)
    return data



def dump_account(account_data):
    db_api = db_handler.db_handler()
    data = db_api("update accounts where account=%s" % account_data['id'],account_data=account_data)
    return True