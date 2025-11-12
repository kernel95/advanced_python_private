# daomod_investigation.py


from member_manager import MemberDao, Member


dao = MemberDao("./testdb.db")

members = dao.get_all()
dao.create_schema()

m = Member(-1, "Alice", "alice@gmail.com", True)
m = dao.add(m)

for member in members:
    print(member)

dao.close()
