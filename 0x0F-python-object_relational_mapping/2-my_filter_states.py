#!/usr/bin/python3
"""takes in an argument and displays all values in the
   states table of hbtn_0e_0_usa where name matches the argument
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    data = cur.fetchall()
    for state in data:
        if state[1] == sys.argv[4]:
            print(state)
    cur.close()
    db.close()
