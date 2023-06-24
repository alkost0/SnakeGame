
class Element:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, __value) -> bool:
        return self.x == other.x and self.y == other.y


