#!/usr/bin/python3
""" Changes the name of the State where id = 2 to New Mexico
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
            if state.id == 2:
                state.name = 'New Mexico'
        conn.commit()
        conn.close()
