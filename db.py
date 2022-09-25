import sqlite3


def connect():
    try:
        con = sqlite3.connect("db/mini_database.db")
        print("connected")
        con.commit()

    except:
        print("failed to connect")
    con.close()


def insertRecord(id, datetime , name, phone, total, product):
    try:
        con = sqlite3.connect("db/mini_database.db")
        cur = con.cursor()
        cur.execute("INSERT INTO store VALUES(?,?,?,?,?,?)", (id, datetime, name, phone, total, product))
        print("stored")
        con.commit()


    except:
        print("failed")

    con.close()

def adminInsert1(ID, NAME ,QTY, RATE):
    try:
        con = sqlite3.connect("db/mini_database.db")
        cur = con.cursor()
        cur.execute("INSERT INTO cosmetics VALUES(?,?,?,?)", (ID, NAME, QTY, RATE))
        print("registered")
        con.commit()



    except:
        print("failed")

    con.close()


def RePrint(ID, reciept):
    try:
        con = sqlite3.connect("db/mini_database.db")
        cur = con.cursor()
        cur.execute("INSERT INTO reprint VALUES(?,?)", (ID , reciept))
        print("reprint stored")
        con.commit()


    except:
        print("failed")

    con.close()