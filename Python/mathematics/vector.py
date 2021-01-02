class Vector2:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def get_x(self) -> float:
        return self.x

    def get_y(self) -> float:
        return self.y

    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y

        return Vector2(self.x, self.y)

    def __sub__(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y

        return Vector2(self.x, self.y)

    def __mul__(self, other: float):
        self.x = self.x * other
        self.y = self.y * other

        return Vector2(self.x, self.y)

    def div(self, other: float):
        self.x = self.x / other
        self.y = self.y / other

        return Vector2(self.x, self.y)

    def __repr__(self):
        return '("%f, %f")' % (self.x, self.y)
