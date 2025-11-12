#web_dao.py

import sqlite3
from member_manager import MemberDao
from flask import g

#we want to access the DAO from the web basically
#this class will be used to make sure every db call will be unique not messing up with other calls
class WebDao(MemberDao):
    def __init__(self, filename="./members.db"):
        #super().__init__(filename)
        self.filename = filename
        self.conn = self.get_connection()

    
    def get_connection(self):
        #make sure not multiple sources access the db so this is to make sure it doesn't happen
        if "db" not in g:
            g.db = sqlite3.connect(self.filename, check_same_thread=False)
            g.db.execute("PRAGMA foreign_keys = ON;")
            g.db.execute("PRAGMA journal_mode = WAL;")
            g.db.execute("PRAGMA synchronous = NORMAL;")
            g.db.row_factory = sqlite3.Row  # For dict-like access

        return g.db

    def close(self):
        # Flask will close the database
        pass