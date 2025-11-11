# database_cli.py
#let's create application

from member_dao import MemberDao


#debugging features

dao = MemberDao("member_database.db")

members = dao.get_all()

for member in members:
    print(member.name)



dao.close()