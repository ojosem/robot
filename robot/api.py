import sys

__all__ = ["Robot"]


def validate_coordinate(coord):
    try:
        (coord := int(coord))
    except:
        print("Position must be provided as an integer.")
        sys.exit(1)
    if coord < 0 or coord > 4:
        print("Position must be between 0 and 4.")
        sys.exit(1)
    return True


def test_position(coord):
    if coord < 0 or coord > 4:
        return False
    return True


def update_position(cur_coord, facing):
    if facing in ("north", "east"):
        new_coord = cur_coord + 1
    else:
        new_coord = cur_coord - 1
    if test_position(new_coord):
        return new_coord
    return cur_coord


class Robot:
    def __init__(self, x: int, y: int, facing: str):
        self.x = x
        self.y = y
        self.facing = facing

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if validate_coordinate(x):
            self._x = int(x)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if validate_coordinate(y):
            self._y = int(y)

    @property
    def facing(self):
        return self._facing

    @facing.setter
    def facing(self, facing):
        if facing.lower() in ("north", "east", "south", "west"):
            self._facing = facing.upper()
        else:
            print("The robot can only face NORTH, EAST, SOUTH, or WEST.")
            sys.exit(1)

    def place(self):
        """Place the robot on the board."""
        pass

    def move(self):
        """Move the robot one square in the direction it's facing, if possible."""
        if (facing := self.facing.lower()) in ("north", "south"):
            self.position = (self.x, update_position(self.y, facing))
        else:
            self.position = (update_position(self.x, facing), self.y)
        pass

    def left(self):
        """Rotate the robot counterclockwise 90 degrees."""
        pass

    def right(self):
        """Rotate the robot clockwise 90 degrees."""
        pass

    def report(self):
        """Print the robot's position on the board."""
        print(self)

    def __repr__(self):
        return f"{self.x},{self.y},{self.facing}"
