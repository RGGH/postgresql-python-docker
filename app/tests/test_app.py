
def test_version(setup_database):
    db= setup_database
    db.db_version()


def test_fetch(setup_database):
    db = setup_database
    #db.fetchone("SELECT COUNT(*) FROM users")
    row = db.fetchone("SELECT COUNT(*) FROM users")
    print("Num of records: ", row[0])






