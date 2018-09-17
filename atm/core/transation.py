#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 0019 下午 21:44
# @Author  : xiaoyafei
# @Site    : 
# @File    : transation.py
# @Software: PyCharm

from conf import settings
from core import account

def make_transation(account_data,tran_type,amount,**others):
    amount = float(amount)
    if tran_type in settings.TRANSACTION_TYPE:
        interest = amount * settings.TRANSACTION_TYPE[tran_type]['interest']
        old_balance = account_data['balance']

        if settings.TRANSACTION_TYPE[tran_type]['action'] == 'plus':
            new_blance = old_balance + amount + interest
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_blance = old_balance - amount - interest

            if new_blance < 0:
                print('你的信用卡[%s]额度不足,还有[-%s]，原来的余额为：[%s]' %(account_data['credit'],(amount + interest), old_balance ))
                return
        account_data['balance'] = new_blance
        account.dump_account(account_data)
        return account_data
    else:
        print('交易类型[%s]不存在'%(tran_type))
