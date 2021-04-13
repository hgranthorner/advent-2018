from typing import Dict, Tuple
from functools import reduce


def count_chars(string: str) -> Tuple[int, int]:
    dct: Dict[str, int] = {}
    for char in string:
        if char not in dct:
            dct[char] = 0

        dct[char] += 1

    s = {v for (_, v) in dct.items() if v == 2 or v == 3}

    return (int(2 in s), int(3 in s))


def sum_tups(t1, t2):
    one = t1[0] + t2[0]
    two = t1[1] + t2[1]
    return (one, two)


def part_one(lines: list[str]):
    (twos, threes) = reduce(sum_tups, map(lambda s: count_chars(s), lines))
    return twos * threes


def compare_strings(string1: str, string2: str) -> bool:
    acc = 0
    for i in range(len(string1)):
        if i == acc + 2:
            return False

        if string1[i] == string2[i]:
            acc += 1

    return acc == len(string1) - 1


def part_two(lines: list[str]):
    for i, line in enumerate(lines):
        for compare in lines[i+1:]:
            if compare_strings(line, compare):
                return (line, compare)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(part_two(lines))
