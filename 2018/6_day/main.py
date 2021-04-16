from dataclasses import dataclass, field
from itertools import product
from typing import Union
from pprint import pprint


@dataclass(order=True, frozen=True)
class Point:
    x: int
    y: int

    def distance(self, other) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)


@dataclass(order=True)
class PointMap:
    x: int
    y: int
    owned_by: Union[Point, None] = field(default=None, hash=False)
    distance_from: int = field(default=100_000_000, hash=False)

    def as_point(self):
        return Point(self.x, self.y)


PointDict = dict[Point, set[Point]]


def get_edges(xs):
    return (
        min(xs, key=lambda p: p.y).y,
        min(xs, key=lambda p: p.x).x,
        max(xs, key=lambda p: p.y).y,
        max(xs, key=lambda p: p.x).x
    )


def parse_points(strings: list[str]) -> list[Point]:
    points = []
    for s in strings:
        splt = s.split(', ')
        x = int(splt[0])
        y = int(splt[1].removesuffix('\n'))
        points.append(Point(x, y))

    return sorted(points)


def generate_points(pd: PointDict):
    keys = pd.keys()
    (top, left, bottom, right) = get_edges(keys)
    return [
        Point(x, y)
        for x, y
        in product(range(top, bottom + 1), range(left + 1, right + 2))
    ]


def apply_influence(point: Point, points: list[PointMap]):
    for p in points:
        d = point.distance(p)
        if d < p.distance_from:
            p.distance_from = d
            p.owned_by = point
        elif d == p.distance_from:
            p.owned_by = None
    pass


def group_by_owner(d: PointDict, ps: list[PointMap]):
    for p in ps:
        if p.owned_by is not None:
            d[p.owned_by].add(p.as_point())
    pass


def get_edge_owners(ps: list[PointMap]) -> set[Point]:
    (top, left, bottom, right) = get_edges(ps)
    return {
        p.owned_by
        for p in ps
        if p.owned_by is not None
        and (p.x == left or p.x == right
             or p.y == top or p.y == bottom)
    }


def part_one(input: list[str]):
    points: PointDict = {p: set() for p in parse_points(input)}
    all_points = [PointMap(p.x, p.y) for p in generate_points(points)]
    for point in points:
        apply_influence(point, all_points)
    group_by_owner(points, all_points)
    edge_owners = get_edge_owners(all_points)
    return max(filter(lambda x: x[0] not in edge_owners,
                      map(lambda p: (p[0], len(p[1])), points.items())),
               key=lambda tup: tup[1])


def calculate_distance(ps: list[Point], cs: list[Point]):
    return map(lambda c: (sum([p.distance(c) for p in ps]), c), cs)


def part_two(input: list[str]):
    points: PointDict = {p: set() for p in parse_points(input)}
    all_points = generate_points(points)
    calced_points = calculate_distance(list(points.keys()), all_points)
    filtered_points = filter(lambda tup: tup[0] < 10000, calced_points)
    print(len(list(filtered_points)))


if __name__ == '__main__':
    file_name = 'input.txt'
    try:
        data = []
        with open(file_name) as f:
            data = f.readlines()

        result = part_two(data)
        pprint(result)
    except FileNotFoundError:
        print(f'cannot find file {file_name}')
