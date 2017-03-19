import sqlite3

conn = sqlite3.connect('homeAutomation.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE SWITCH
       (ID INTEGER PRIMARY KEY   AUTOINCREMENT,
       SWITCHNAME           TEXT    NOT NULL,
       PORTNAME            TEXT     UNIQUE);''')
print "Table created successfully";

conn.close()
