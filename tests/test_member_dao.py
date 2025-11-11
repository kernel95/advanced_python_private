# test_member_dao.py


import os
import sqlite3
import pytest
from Member import Member
from member_dao import MemberDao

DBFILENAME="testdb.db"

@pytest.fixture(scope="session")
def db_path(request):
    print("****Creating database")
    path=DBFILENAME
    dao = MemberDao(DBFILENAME)
    dao.create_schema()
    dao.add(Member(-1, "Alice", "alice@gmail.com", True))
    dao.add(Member(-1, "Bob", "bob@gmail.com", False))
    dao.add(Member(-1, "Carol", "carol@gmail.com", False))
    dao.close()

    def cleanup():
        print ("Cleaning up the database")
        # delete the file
        if os.path.exists(path):
            os.remove(path)
            print (f"file {path} removed")

    request.addfinalizer(cleanup)

    return path



# def test_create_schema():

#     dao = MemberDao(DBFILENAME)
#     dao.create_schema()
#     dao.add(Member(-1, "Alice", "alice@gmail.com", True))
#     dao.add(Member(-1, "Bob", "bob@gmail.com", False))
#     dao.add(Member(-1, "Carol", "carol@gmail.com", False))
#     dao.close()


def test_open_close(db_path):

    dao = MemberDao(DBFILENAME)
    dao.close()


def test_get_all():
    dao = MemberDao(DBFILENAME)
    members = dao.get_all()
    assert(len(members)) > 0
    dao.close()


def test_insert_delete():
    member = Member(-1, "New User", "new.user3@gmail.com", True)
    dao = MemberDao(DBFILENAME)
    added_member = dao.add(member)
    dao.delete(added_member.id)
    dao.close()

    assert added_member.id != -1

def test_duplicate_email_fails():

    dao = MemberDao(DBFILENAME)
    m1 = Member(-1, "Aidan", "abcde@gmail.com", True)
    m2 = Member(-1, "Alice", "abcde@gmail.com", False)

    m1 = dao.add(m1)

    # verify that this causes an exception
    with pytest.raises(sqlite3.IntegrityError):
        dao.add(m2)

    dao.delete(m1.id)
    dao.close()

def test_update():
    dao = MemberDao(DBFILENAME)
    member = Member(-1, "Alice", "abcdefghi@gmail.com", False)
    member = dao.add(member)
    member.name = "CHANGED"
    member.email = "changedd@gmail.com"
    member.active = not member.active

    dao.update(member)

    members = dao.get_all()
    assert members[-1] == member

    dao.delete(member.id)

    dao.close()


def test_change_to_existing_email():

    dao = MemberDao(DBFILENAME)

    member1 = dao.add(Member(-1, "Test1", "test1@gmail.com", True))
    member2 = dao.add(Member(-1, "Test2", "test2@gmail.com", True))

    member2.email = member1.email

    # this should raise a ValueError
    with pytest.raises(ValueError):
        dao.update(member2)

    dao.delete(member1.id)
    dao.delete(member2.id)

    dao.close()

def test_add_names_with_apostrophes():

    dao = MemberDao(DBFILENAME)
    member = Member(-1, "Alice O'Sullivan", "aliceos@gmail.com", True)
    member = dao.add(member)

    
    assert member.id != -1
    dao.close()

#def test_sql_injection(db_path):
#    dao = MemberDao(DBFILENAME)    
    
#    member = Member(-1, "','',0); --", "", True)

#    member = dao.add(member)
#    assert member.id != -1
#   dao.close()

def test_update_names_with_apostrophes():

    dao = MemberDao(DBFILENAME)
    member = dao.add(Member(-1, "Zoe", "zoe1@gmail.com", True))
    member.name = "Zoe O'Sullivan"
    dao.update(member)