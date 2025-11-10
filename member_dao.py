# member_dao.py

# data access object for reading and writing to member database
import sqlite3
from dataclasses import dataclass

from Member import Member,members


@dataclass
class MemberDao():
    filename: str =  "member_database_trainer.db"

    def __init__(self):
        self.conn = sqlite3.connect(self.filename)
    
    def get_all(self)->list[Member]:
        members:list[Member] = []
        cursor = self.conn.cursor()
        sql = "SELECT * FROM members"
        rs = cursor.execute(sql)

        for row in rs:
            (id, name, email, active) = row
            member = Member(id, name, email, active)

            members.append(member)
        return members
    
    def add(self, member):
        
        sql = f"""INSERT INTO members 
                (name, email, active) 
                VALUES(
                    '{member.name}', 
                    '{member.email}', 
                    {1 if member.active else 0}
                )"""
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()

        # read the newly generated id from the db
        member.id = cursor.lastrowid
        return member
    
    def delete(self, id):
        sql = f"""DELETE FROM members WHERE id = {id}"""
        cursor = self.conn.cursor()
        cursor.execute(sql)
        cursor.conn.commit()

        return cursor.rowcount


        


    def close(self):
        self.conn.close()

if __name__ == "__main__":

    dao = MemberDao()
    members = dao.get_all()

    for member in members:
        print (member)