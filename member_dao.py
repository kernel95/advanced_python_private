# member_dao.py

# data access object for reading and writing to member database
import sqlite3
from dataclasses import dataclass

from Member import Member


@dataclass
class MemberDao():
    filename: str

    def __init__(self, filename="member_database.db"):
        self.filename = filename
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
        self.conn.commit()

        return cursor.rowcount
        
    def update(self, member):
        try:
            sql = f"""UPDATE members 
                SET 
                    name = '{member.name}', 
                    email='{member.email}', 
                    active={1 if member.active else 0} 
                WHERE id = {member.id}"""
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
        except sqlite3.IntegrityError:
            # user with this email already exists
            raise ValueError("User with this email already exists")


    def close(self):
        self.conn.close()

    def create_schema(self):
        sql = """
                CREATE TABLE IF NOT EXISTS members (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    active BOOLEAN NOT NULL
                );
                """
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()



if __name__ == "__main__":

    dao = MemberDao()
    members = dao.get_all()

    for member in members:
        print (member)