#!/usr/bin/python3

''' This script lists alll staes from hbtn DB '''

import sys
import MySQLdb


def main():
    ''' this function executes when called '''

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name CONTAINS "N" ORDER BY id ASC')
    result = cur.fetchall()
    for row in result:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
