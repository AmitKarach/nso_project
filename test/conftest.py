import db.db as db


def pytest_runtest_setup():
    # code to run before each test
    db.delete_messages_from_db()