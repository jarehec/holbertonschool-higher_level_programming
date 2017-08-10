#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa
"""
if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    if len(sys.argv) == 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                                sys.argv[1], sys.argv[2], sys.argv[3]))
        conn = engine.connect()
        result = conn.execute("SELECT * FROM states ORDER BY states.id ASC")
        for state in result:
            print(state)
        conn.close()
