#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities of that
   states using the hbtn_0e_4_usa database
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    if len(sys.argv) == 5:
        s_list = []
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
        cur = db.cursor()
        cur.execute("SELECT * FROM states,cities \
                    WHERE states.id=cities.state_id \
                    ORDER BY cities.id ASC")
        table = cur.fetchall()
        for state in table:
            if state[1] == sys.argv[4]:
                s_list.append(state[4])
        print(', '. join(s_list))
        cur.close()
        db.close()
