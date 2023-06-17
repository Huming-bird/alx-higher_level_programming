#!/usr/bin/python3

''' this script uses SQLAlchemy ORM to cretae table like classes '''

import MySQLdb
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

db_query = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
user = sys.argv[1]
pwd = sys.argv[2]
db = sys.argv[3]


def main():
    ''' this function fetches all states from the db '''

    engine = create_engine(db_query.format(user, pwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()


if __name__ == '__main__':
    main()
