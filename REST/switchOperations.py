import sqlite3
try:
    conn = sqlite3.connect('database/homeAutomation.db')
except Exception as e:
    print e

def addSwitchInDb(switch,port):
    qry = 'INSERT INTO SWITCH (SWITCHNAME,PORTNAME) VALUES("'+switch+'","'+port+'");'
    try:
        conn.execute(qry);
    except ValueError as e:
        print "DUPLICATE"
        pass
    conn.commit()
