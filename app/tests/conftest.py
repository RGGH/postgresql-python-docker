import pytest
from app.db_con import dbConnection

@pytest.fixture(scope= "module")
def setup_database():
    """ Fixture to set up the table test data """
    db = dbConnection()
    return db
