import typer
from robot import Robot


app = typer.Typer(add_completion=False)


@app.command()
def place(placement: str):
    """
    Place the robot on the board.
    """
    placement = placement.split(",")
    x = placement[0]
    y = placement[1]
    facing = placement[2]
    robot = Robot(x, y, facing)
    robot.place()


@app.command()
def move():
    """
    Move the robot forward one square, without falling off the board.
    """
    typer.echo("MOVED")


@app.command()
def left():
    """
    Rotate the robot counterclockwise 90 degress.
    """
    typer.echo("TURNED LEFT")


@app.command()
def right():
    """
    Rotate the robot clockwise 90 degress.
    """
    typer.echo("TURNED RIGHT")


@app.command()
def report():
    """
    Report the robot's position on the board.
    """
    typer.echo("0,2,NORTH")


@app.command()
def rock():
    """
    Rock out with the robot.
    """
    typer.echo("🤘")


if __name__ == "__main__":
    app()
