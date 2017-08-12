#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa
"""
if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    if len(sys.argv) == 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                               (sys.argv[1], sys.argv[2], sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        conn = Session()
        for state in conn.query(State).order_by(State.id).all():
            print("{}: {}".format(state.id, state.name))
        conn.close()
