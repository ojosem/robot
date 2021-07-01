from tinydb.database import TinyDB
from robot import __version__, Robot
from tinydb import TinyDB

import pytest


def test_version():
    assert __version__ == "0.1.0"


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


def test_place(robot_db, db_path):
    db = robot_db
    input_ = "1,3,NORTH"
    Robot.place(input_, db_path)
    assert db.all()[0]["x"] == 1
    assert db.all()[0]["y"] == 3
    assert db.all()[0]["facing"] == "NORTH"


def test_move_north(robot_db, db_path):
    db = robot_db
    db.insert({"x": 0, "y": 3, "facing": "NORTH"})
    Robot.move(db_path)
    assert db.all()[0]["x"] == 0
    assert db.all()[0]["y"] == 4
    assert db.all()[0]["facing"] == "NORTH"
    Robot.move(db_path)
    assert db.all()[0]["x"] == 0
    assert db.all()[0]["y"] == 4
    assert db.all()[0]["facing"] == "NORTH"


def test_move_south(robot_db, db_path):
    db = robot_db
    db.insert({"x": 0, "y": 1, "facing": "SOUTH"})
    Robot.move(db_path)
    assert db.all()[0]["x"] == 0
    assert db.all()[0]["y"] == 0
    assert db.all()[0]["facing"] == "SOUTH"
    Robot.move(db_path)
    assert db.all()[0]["x"] == 0
    assert db.all()[0]["y"] == 0
    assert db.all()[0]["facing"] == "SOUTH"


def test_move_east(robot_db, db_path):
    db = robot_db
    db.insert({"x": 3, "y": 1, "facing": "EAST"})
    Robot.move(db_path)
    assert db.all()[0]["x"] == 4
    assert db.all()[0]["y"] == 1
    assert db.all()[0]["facing"] == "EAST"
    Robot.move(db_path)
    assert db.all()[0]["x"] == 4
    assert db.all()[0]["y"] == 1
    assert db.all()[0]["facing"] == "EAST"


def test_move_west(robot_db, db_path):
    db = robot_db
    db.insert({"x": 1, "y": 1, "facing": "WEST"})
    Robot.move(db_path)
    assert db.all()[0]["x"] == 0
    assert db.all()[0]["y"] == 1
    assert db.all()[0]["facing"] == "WEST"
    Robot.move(db_path)
    assert db.all()[0]["x"] == 0
    assert db.all()[0]["y"] == 1
    assert db.all()[0]["facing"] == "WEST"


def test_rotate_left(robot_db, db_path):
    db = robot_db
    db.insert({"x": 0, "y": 0, "facing": "NORTH"})
    Robot.rotate("LEFT", db_path)
    assert db.all()[0]["facing"] == "WEST"
    Robot.rotate("LEFT", db_path)
    assert db.all()[0]["facing"] == "SOUTH"
    Robot.rotate("LEFT", db_path)
    assert db.all()[0]["facing"] == "EAST"
    Robot.rotate("LEFT", db_path)
    assert db.all()[0]["facing"] == "NORTH"


def test_rotate_right(robot_db, db_path):
    db = robot_db
    db.insert({"x": 0, "y": 0, "facing": "NORTH"})
    Robot.rotate("RIGHT", db_path)
    assert db.all()[0]["facing"] == "EAST"
    Robot.rotate("RIGHT", db_path)
    assert db.all()[0]["facing"] == "SOUTH"
    Robot.rotate("RIGHT", db_path)
    assert db.all()[0]["facing"] == "WEST"
    Robot.rotate("RIGHT", db_path)
    assert db.all()[0]["facing"] == "NORTH"
