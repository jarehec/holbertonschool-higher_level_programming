#!/usr/bin/python3
"""takes in an argument and displays all values in the
   states table of hbtn_0e_0_usa where name matches the argument
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    if len(sys.argv) == 5:
        user = sys.argv[1]
        passwd = sys.argv[2]
        database = sys.argv[3]
        match = sys.argv[4]
        s_list = []
        db = MySQLdb.connect(host="localhost", user=user, passwd=passwd,
                             db=database, port=3306)
        cur = db.cursor()
        cur.execute("SELECT * FROM states,cities \
                    WHERE states.id=cities.state_id \
                    ORDER BY cities.id ASC")
        table = cur.fetchall()
        for state in table:
            if state[1] == match:
                s_list.append(state[4])
        print(', '. join(s_list))
        cur.close()
        db.close()
