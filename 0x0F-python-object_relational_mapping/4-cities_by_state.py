#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    if len(sys.argv) == 4:
        user = sys.argv[1]
        passwd = sys.argv[2]
        database = sys.argv[3]
        db = MySQLdb.connect(host="localhost", user=user, passwd=passwd,
                             db=database, port=3306)
        cur = db.cursor()
        cur.execute("SELECT cities.id, cities.name, states.name \
                    FROM cities, states WHERE states.id=cities.state_id \
                    ORDER BY cities.id ASC")
        table = cur.fetchall()
        for state in table:
            print(state)
        cur.close()
        db.close()
