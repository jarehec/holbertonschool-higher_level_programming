#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)
   from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost", user=user, passwd=passwd,
                         db=database, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    data = cur.fetchall()
    for state in data:
        if state[1][0] == 'N':
            print(state)
    cur.close()
    db.close()
