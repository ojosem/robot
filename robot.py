from dataclasses import dataclass

__all__ = ["Robot"]


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


@dataclass
class Robot:
    position: tuple[int, int]
    facing: str

    def move(self):
        x = self.position[0]
        y = self.position[1]
        facing = self.facing.lower()
        if facing in ("north", "south"):
            self.position = (x, update_position(y, facing))
        else:
            self.position = (update_position(x, facing), y)

    def __repr__(self):
        return f"{self.position[0]},{self.position[1]},{self.facing.upper()}"
