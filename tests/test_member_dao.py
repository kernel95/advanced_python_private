#test_member_dao.py

from Member import Member
from member_dao import MemberDao


def test_open_close():
    dao = MemberDao()
    dao.close()
    
def test_get_all():
    dao = MemberDao()
    #test to check if my variable is empty so if function get is working
    members = dao.get_all()
    assert(len(members)) > 0
    dao.close()

def test_insert_delete():
    member = Member(-1, "New User3", "new.user3@gmail.com", True)
    dao = MemberDao()
    added_member = dao.add(member)
    dao.close()
    assert added_member.id != -1

    dao.delete(added_member.id)
    dao.close
    assert added_member.id != -1