import pytest
from tinydb import TinyDB


@pytest.fixture(scope="module")
def db_dir(tmp_path_factory):
    """A temp dir for the db"""
    return tmp_path_factory.mktemp("tmp_db_dir")


@pytest.fixture(scope="module")
def db_path(db_dir):
    """A db that can be used for all tests"""
    return db_dir / "db.json"


@pytest.fixture(scope="module")
def db_module(db_path):
    """A db that can be used for all tests"""
    return TinyDB(db_path)


@pytest.fixture()
def robot_db(db_module):
    db_module.truncate()
    return db_module
