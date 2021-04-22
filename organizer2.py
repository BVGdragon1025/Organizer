import sqlite3
import os
conn = sqlite3.connect("organizer.db")

if not os.path.exists("organizer.db"):
    conn.execute("CREATE TABLE 'notes'("
                 "'id' INTEGER NOT NULL,"
                 "'title' TEXT NOT NULL,"
                 "PRIMARY KEY('id' AUTOINCREMENT);")
    conn.execute("CREATE TABLE 'tasks'("
                 "'id' INTEGER NOT NULL,"
                 "'title' TEXT NOT NULL,"
                 "'exp_date' TEXT NOT NULL,"
                 "PRIMARY KEY('id' AUTOINCREMENT);")