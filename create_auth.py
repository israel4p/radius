#!/usr/bin/env python3

import sys

import pymysql


def create(user_pppoe, passwd_pppoe):

    con = pymysql.connect(
        host='localhost', user='user_db', passwd='passwd_db', db='radius')

    db = con.cursor()

    query = "SELECT * FROM radcheck WHERE username='%s' and value='%s'"
    db.execute(query % (user_pppoe, passwd_pppoe))

    data = db.fetchone()

    if not data:
        query = "INSERT INTO radcheck (username, value) VALUES('%s', '%s')"
        db.execute(query % (user_pppoe, passwd_pppoe))

        con.commit()
    else:
        print("Accept")

    con.close()


try:
    user = sys.argv[1].strip()
    passwd = sys.argv[2].strip()
except IndexError:
    pass
else:
    create(user, passwd)
