#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 0019 下午 18:03
# @Author  : xiaoyafei
# @Site    : 
# @File    : main.py
# @Software: PyCharm

from core import shopping_mall
from core import auth
from core import account
from core import transation

def account_info(acc_data):
    account_data = account.load_current_balance(acc_data['account_id'])
    data_info = '''
        账号ID：%s,
        密码：%s,
        信用额度：%s,
        剩余额度：%s,
        账号注册时间：%s,
        账号过期时间:%s,
        每月还款日：%s
    '''%(account_data['id'],account_data['password'],account_data['credit'],account_data['balance'],account_data['enroll_data'],account_data['expire_data'],account_data['pay_day'])
    print(data_info)

def pay_back(acc_data):  # 还钱
    account_data = account.load_current_balance(acc_data['account_id'])
    current_balance = '''
        Credit:%s
        Balance:%s
    '''%(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input('请输入你要还的金额：').strip()
        if len(repay_amount)>0 and repay_amount.isdigit():
            new_blance = transation.make_transation(account_data,'repay', repay_amount)
            if new_blance:
                print('最新可用额度[%s]'%(new_blance['balance']))
        else:
            print('[%s]输入有误，只支持整数'%(repay_amount))

        if repay_amount == 'b':
            back_flag = True


def withdraw(acc_data):
    account_data = account.load_current_balance(acc_data['account_id'])
    current_balance = '''--------- BALANCE INFO --------
        Credit:%s
        Balance:%s
    '''%(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input('请输入取款金额：').strip()
        if len(withdraw_amount)>0 and withdraw_amount.isdigit():
            new_blance = transation.make_transation(account_data,'withdraw', withdraw_amount)
            if new_blance:
                print('最新可用额度[%s]'%(new_blance['balance']))
        else:
            print('[%s]输入有误，只支持整数'%(withdraw_amount))

        if withdraw_amount == 'b':
            back_flag = True

def shopping(acc_data):
    product_list = [
        ['IphoneX',8388],
        ['iPhone 8',5399],
        ['Python Book',99],
        ['Coffee',33],
        ['Bike',666],
        ['pen',2]
    ]

    shopping_cart = []
    count = 0
    salary = acc_data['account_data']['balance']
    while True:
        account_data = account.load_current_balance(acc_data['account_id'])
        print('>>欢迎来到本商城 您的余额是[%s]元。<<'%salary)
        for index,i in enumerate(product_list):
            print("%s.\t%s\t%s" % (index, i[0], i[1]))
        choice = input('>>请输入商品编号 exit退出商城<<')
        if len(choice)== 0:
            print('你没有选择商品')
            continue
        if choice.isdigit():
            choice = int(choice)
            if choice < len(product_list) and choice >= 0:
                item  = product_list[choice]
                if salary >= item[1]:
                    salary -= item[1]
                    shopping_cart.append(item)
                    print("添加 \033[32;1m%s\033[0m 到购物车,您目前的金额是 \
                        \033[31;1m%s\033[0m" % (item[0], salary))
                else:
                    print("对不起，您的金额不足,还差 \033[31;1m%s\033[0m" % (item[1] - salary,))
            else:
                print('没有此商品')
        elif choice == 'exit':
            total_cost = 0
            print('你的购物车列表：')
            for i in shopping_cart:
                print(i)
                total_cost += i[1]
            print("您的购物车总价是: \033[31;1m%s\033[0m" % (total_cost,))
            print("您目前的余额是: \033[31;1m%s\033[0m" % (salary,))
            new_balance = transation.make_transaction(account_data, 'withdraw', total_cost)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))
            break



def logout(acc_data):
    exit()




user_data = {
    'account_id':None,
    'is_authenticated':False,  #  默认没有登陆
    'account_data':None
}

def menu(acc_data):
    menu = '''
        ----------中国人民银行----------
        1.账户信息
        2.还款
        3.取款
        6.商城
        7.退出
    '''
    menu_dic = {
        '1':account_info,
        '2':pay_back,
        '3':withdraw,
        '6': shopping,
        '7':logout

    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        choice = input('>>').strip()
        if choice in menu:
            menu_dic[choice](acc_data)



def run():
    # 默认没有登陆，让用户进行登陆
    acc_data = auth.acc_auth(user_data)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        menu(user_data)




