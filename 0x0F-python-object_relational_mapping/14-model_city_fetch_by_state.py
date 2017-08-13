#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa
"""
if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from model_city import Base, City
    from model_state import State
    from sqlalchemy.orm import sessionmaker
    if len(sys.argv) == 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                               (sys.argv[1], sys.argv[2], sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        conn = Session()
        for city in conn.query(City, State).order_by(City.id).all():
            if city.City.state_id == city.State.id:
                print("{}: ({}) {}".format(city.State.name,
                                           city.City.id, city.City.name))
