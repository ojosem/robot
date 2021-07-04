from robot import app
from typer.testing import CliRunner

runner = CliRunner()


def test_place_good_input():
    result = runner.invoke(app, ["place", "1,4,NORTH"])
    assert result.exit_code == 0
    assert result.stdout == ""


def test_place_bad_input():
    result = runner.invoke(app, ["place", "1,4,NORYH"])
    assert result.exit_code == 1
    assert result.stdout == "The robot can only face NORTH, SOUTH, EAST, or WEST.\n"


def test_place_extra_input():
    result = runner.invoke(app, ["place", "1,4,", "EAST"])
    assert result.exit_code == 2
    assert result.stdout == (
        "Usage: root place [OPTIONS] PLACEMENT\nTry 'root place --help' for help.\n\nError: Got unexpected extra argument (EAST)\n"
    )


def test_report():
    result = runner.invoke(app, ["report"])
    assert result.exit_code == 0


def test_move():
    result = runner.invoke(app, ["move"])
    assert result.exit_code == 0


def test_rotate_left():
    result = runner.invoke(app, ["left"])
    assert result.exit_code == 0


def test_rotate_left():
    result = runner.invoke(app, ["right"])
    assert result.exit_code == 0
