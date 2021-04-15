from datetime import datetime, time, timedelta
from pprint import pprint

from dataclasses import dataclass, field
import re

Guards = dict[int, dict[time, int]]
GuardsWithSleepAmount = list[tuple[int, dict[int, dict[time, int]]]]


@dataclass(order=True)
class Line:
    timestamp: datetime
    remainder: str = field(compare=False)

    @classmethod
    def from_split_line(cls, dt: str, rest: str):
        return cls(datetime.strptime(dt, "%Y-%m-%d %H:%M"), rest)


timestamp_regex = re.compile(r'\[(.*)]\s(.*)')


def datetime_range(start: datetime, end: datetime, delta: timedelta):
    current = start
    while current < end:
        yield current
        current += delta


def order_input(input: list[str]):
    lines: list[Line] = []
    for l in input:
        grps = timestamp_regex.match(l).groups()
        lines.append(Line.from_split_line(grps[0], grps[1]))

    lines.sort()
    return lines


begin_shift_regex = re.compile(r'.*\s#(\d+)')


def parse_remainder(lines: list[Line]):
    guards: Guards = {}
    id = 0
    guard = {}
    sleepy_start = datetime.today()
    for line in lines:
        guard_match = begin_shift_regex.match(line.remainder)
        if guard_match is not None:
            id = int(guard_match.groups()[0])
            if id not in guards:
                guards[id] = {}
            guard = guards[id]

        elif line.remainder == 'falls asleep':
            sleepy_start = line.timestamp
        else:
            sleepy_end = line.timestamp
            sleep_range = list(datetime_range(
                sleepy_start, sleepy_end, timedelta(minutes=1)))
            for time in map(lambda dt: dt.time(), sleep_range):
                if time in guard:
                    guard[time] += 1
                else:
                    guard[time] = 1

    return guards


def find_sleepiest_guard(guards: Guards):
    # Should transform our dict of id -> sleepy times
    # To a list of tuples: [(amount of sleep, {id: sleepy_times})]
    # Then we find the max of the list

    tup: GuardsWithSleepAmount = [
        (sum(v.values()), {k: v})
        for (k, v)
        in guards.items()
    ]

    max = 0
    id = -1

    for (amount, guard) in tup:
        if amount > max:
            max = amount
            id = list(guard.keys())[0]

    return (max, id)


def most_often_asleep(id: int, data: Guards):
    pprint(data)
    guard = data[id]
    return max(list(guard.items()), key=lambda x: x[1])


def part_one(lines: list[str]):
    ordered = order_input(lines)
    guard_data = parse_remainder(ordered)
    (_, guard_id) = find_sleepiest_guard(guard_data)
    minute = most_often_asleep(guard_id, guard_data)
    return (minute, guard_id)


if __name__ == '__main__':
    file_name = 'input.txt'
    try:
        with open(file_name) as f:
            pprint(part_one(f.readlines()))
    except FileNotFoundError:
        print(f'Could not find {file_name}')
