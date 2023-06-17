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
    state_name = sys.argv[4]

    db = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db)
    cur = db.cursor()
    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id =\
            states.id WHERE states.name = '{}' ORDER BY cities.id ASC"
    cur.execute(query.format(state_name))
    result = cur.fetchall()
    for row in result:
        if row != result[-1]:
            print(row[0], end=', ')
        else:
            print(row[0])

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
