from robot import __version__, Robot
import pytest


def test_version():
    assert __version__ == "0.1.0"


class TestMove:
    def test_move_north(self):
        robot = Robot(0, 1, "NORTH")
        robot.move()
        assert robot.position == (0, 2)

    def test_move_east(self):
        robot = Robot(4, 4, "EAST")
        robot.move()
        assert robot.position == (4, 4)

    def test_move_south(self):
        robot = Robot(0, 0, "SOUTH")
        robot.move()
        assert robot.position == (0, 0)

    def test_move_west(self):
        robot = Robot(2, 2, "WEST")
        robot.move()
        assert robot.position == (1, 2)
