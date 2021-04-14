from dataclasses import dataclass
import re


@dataclass
class Claim:
    id: int
    fromLeft: int
    fromTop: int
    width: int
    height: int

    def top_left():
        pass

    def bottom_right():
        pass

    @classmethod
    def from_string(cls, string: str):
        pattern = r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)'
        [id, l, t, w, h] = re.search(pattern, string).groups()
        return cls(int(id), int(l), int(t), int(w), int(h))


def find_intersection(claim1: Claim, claim2: Claim):
    pass
    # x_dist = (min(r1[x], r2[x]) -
    #           max(l1[x], l2[x]))

    # y_dist = (min(r1[y], r2[y]) -
    #           max(l1[y], l2[y]))


def part_one():
    pass


def part_two():
    pass


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            claim = Claim.from_string(line)
            print(claim)
