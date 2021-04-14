from dataclasses import dataclass
from itertools import product
import re
from typing import Iterable

# origin is (0,0), increasing down and to the right


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass
class Claim:
    id: int
    from_left: int
    from_top: int
    width: int
    height: int

    def top_left(self) -> Point:
        return Point(self.from_left, self.from_top)

    def bottom_left(self) -> Point:
        return Point(self.from_left, self.from_top + self.height)

    def top_right(self) -> Point:
        return Point(self.from_left + self.width, self.from_top)

    def bottom_right(self) -> Point:
        return Point(self.from_left + self.width,
                     self.from_top + self.height)

    @classmethod
    def from_string(cls, string: str):
        pattern = r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)'
        [id, l, t, w, h] = re.search(pattern, string).groups()
        return cls(int(id), int(l), int(t), int(w), int(h))


def generate_points(claim: Claim) -> Iterable[Point]:
    top_left = claim.top_left()
    min_x, min_y = top_left.x, top_left.y
    bottom_right = claim.bottom_right()
    max_x, max_y = bottom_right.x, bottom_right.y

    point_product = product(range(min_x, max_x), range(min_y, max_y))
    return [Point(x, y) for (x, y) in point_product]


def part_one(lines: list[str]):
    claims = [Claim.from_string(x) for x in lines]
    d: dict[Point, int] = {}

    for claim in claims:
        points = generate_points(claim)
        upsert_points(d, points)

    return len([v for (_, v) in d.items() if v > 1])


def part_two(lines: list[str]):
    claims = [Claim.from_string(x) for x in lines]
    d: dict[Point, int] = {}
    claim_dict: dict[int, list[Point]] = {}

    for claim in claims:
        points = list(generate_points(claim))
        claim_dict[claim.id] = points
        upsert_points(d, points)

    for claim in claims:
        counts = [d[p] for p in claim_dict[claim.id]]
        if len([x for x in counts if x > 1]) == 0:
            return claim.id


def upsert_points(d: dict[Point, int], points: Iterable[Point]):
    for point in points:
        if point in d:
            d[point] += 1
        else:
            d[point] = 1


if __name__ == '__main__':
    file_name = 'input.txt'
    try:
        with open(file_name) as f:
            print(part_two(f.readlines()))

    except FileNotFoundError:
        print(f'{file_name} not found')
