#!/usr/bin/python3

''' This script lists alll staes from hbtn DB '''

import sys
import MySQLdb


def main():
    ''' this function executes when called '''

    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    db = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '%N%' ORDER BY id ASC"
    cur.execute(query)
    result = cur.fetchall()
    for row in result:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    main()