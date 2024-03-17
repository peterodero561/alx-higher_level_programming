#!/usr/bin/python3
'''Prints the first State object from a given database'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def addState(username, password, database):
    '''prints first state of a database'''
    # create engine
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(username, password, database), pool_pre_ping=True)

    # bind engine to the metadata of the base class
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # create new object and add to session
    newState = State(name='Louisiana')
    session.add(newState)

    # commit
    session.commit()

    # query
    states = session.query(State).filter(State.name.like('Louisiana')).all()

    # print output
    if states:
        for state in states:
            print("{}".format(state.id))
    else:
        print("Not found")

    # close session
    session.close()


if __name__ == '__main__':
    if (len(sys.argv) < 4):
        print('Usage: ./11-model_state.py username, password, database')
        sys.exit(1)

    # assignement
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # call function
    addState(username, password, database)
