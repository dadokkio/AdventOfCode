inp = open("input.txt", "r").read().strip()


class Brick:
    def __init__(self, line: str) -> None:
        c0, c1 = [[int(x) for x in c.split(",")] for c in line.split("~")]
        self.xrange = set(range(c0[0], c1[0] + 1))
        self.yrange = set(range(c0[1], c1[1] + 1))
        self.h0: int = c0[2]
        self.h1: int = c1[2]
        self.supp: list[Brick] = []
        self.rest: list[Brick] = []
        self.falling = False

    def minheight(self) -> int:
        return min(self.h0, self.h1)

    def maxheight(self) -> int:
        return max(self.h0, self.h1)

    def overlaps(self, b: "Brick") -> bool:
        return bool(self.xrange & b.xrange and self.yrange & b.yrange)

    def recursive_fall(self) -> int:
        self.falling = True
        s = 0
        for x in self.supp:
            if not [y for y in x.rest if not y.falling]:
                s += 1
                s += x.recursive_fall()
        return s


def drop(bricks: list[Brick]):
    for n, b in enumerate(bricks):
        for x in range(n - 1, -1, -1):
            rest_height = b.rest[0].maxheight() if b.rest else 1
            if b.overlaps(bricks[x]):
                new_height = bricks[x].maxheight()
                if not b.rest or new_height > rest_height:
                    for y in b.rest:
                        y.supp.remove(b)
                    b.rest = [bricks[x]]
                    bricks[x].supp.append(b)
                elif new_height == rest_height:
                    b.rest.append(bricks[x])
                    bricks[x].supp.append(b)
        height_diff = (
            b.minheight() - (b.rest[0].maxheight() + 1) if b.rest else b.minheight() - 1
        )
        b.h0 -= height_diff
        b.h1 -= height_diff


bricks: list[Brick] = []
[bricks.append(Brick(line)) for line in inp.splitlines()]
bricks = sorted(bricks, key=lambda b: b.minheight())
drop(bricks)
tot = sum(all((len(x.rest) > 1 for x in b.supp)) for b in bricks)
print(tot)

tot = 0
for b in bricks:
    for x in bricks:
        x.falling = False
    tot += b.recursive_fall()
print(tot)
