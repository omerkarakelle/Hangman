import sqlite3
from random import randint

"""def openConnection():
    global connection
    connection = sqlite3.connect("datab.db")
    global cursor
    cursor = connection.cursor()"""
connection = sqlite3.connect("datab.db")
cursor = connection.cursor()
def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS game (Word TEXT, Definition TEXT)")
    connection.commit()
def addWord(word,df):
    cursor.execute("INSERT INTO game VALUES(?,?)",(word,df))
    connection.commit()
def pickAWord():
    global connection
    connection = sqlite3.connect("datab.db")
    global cursor
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM game")
    list = cursor.fetchall()
    connection.commit()
    connection.close()
    return list[randint(0,len(list)-1)]
def updateData(oldWord,newWord):
    cursor.execute("UPDATE game SET Word = '?' WHERE Word = '?'",(newWord,oldWord))
    connection.commit()
"""def closeConnection():
    connection.close()"""