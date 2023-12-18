data = open("input.txt").read().split()


class Beam:
    def __init__(self, x, y, dx, dy):
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy

    def move(self):
        m = data[self.y][self.x]
        if m == "-" and self.dy != 0:
            return [Beam(self.x, self.y, -1, 0), Beam(self.x, self.y, +1, 0)]
        elif m == "|" and self.dx != 0:
            return [Beam(self.x, self.y, 0, -1), Beam(self.x, self.y, 0, +1)]
        elif m == "/":
            t = self.dx
            self.dx = -self.dy
            self.dy = -t
        elif m == "\\":
            t = self.dx
            self.dx = self.dy
            self.dy = t

        self.x += self.dx
        self.y += self.dy
        return [self]


def count(x, y, dx, dy):
    beams = [Beam(x, y, dx, dy)]
    energized = {(x, y, dx, dy)}

    while beams != []:
        new_beams = []
        for b in beams:
            energized.add((b.x, b.y, b.dx, b.dy))
            new_beams += b.move()
        beams = [
            b
            for b in new_beams
            if b.x >= 0
            and b.x < len(data[0])
            and b.y >= 0
            and b.y < len(data)
            and (b.x, b.y, b.dx, b.dy) not in energized
        ]

    return len({(x, y) for (x, y, _, _) in energized})


if __name__ == "__main__":
    print(count(0, 0, +1, 0))
