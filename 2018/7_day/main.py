import re
from pprint import pprint
from dataclasses import dataclass
from typing import Union
from sortedcontainers import SortedSet

Requirements = dict[str, set[str]]


@dataclass(frozen=True, order=True)
class StepPair:
    first: str
    second: str

    @classmethod
    def from_input_regex(cls, matches: Union[re.Match[str], None]):
        return cls(matches[1], matches[2])


def build_requirements(pairs: list[StepPair]) -> Requirements:
    reqs: Requirements = {
        s.second: {f.first for f in pairs if f.second == s.second}
        for s in pairs
    }

    for s in [p.first for p in pairs if p.first not in reqs]:
        reqs[s] = set()

    return reqs


def build_execution_order(reqs: Requirements) -> str:
    order: list[str] = []
    completed_steps: set[str] = set()
    available_steps = SortedSet()
    num_keys = len(reqs.keys())
    while len(order) < num_keys:
        for (step, req_set) in reqs.items():
            if req_set <= completed_steps and step not in completed_steps:
                available_steps.add(step)

        next_step: str = str(available_steps[0])
        available_steps.remove(next_step)
        order.append(next_step)
        completed_steps.add(next_step)

    return ''.join(order)


input_parse_regex = re.compile(r'Step\s(.).*step\s(.)')


def part_one(input: list[str]):
    parsed = [StepPair.from_input_regex(
        input_parse_regex.match(s)) for s in input]
    reqs: Requirements = build_requirements(parsed)
    execution_order = build_execution_order(reqs)
    pprint(execution_order)


if __name__ == '__main__':
    file_name = 'input.txt'

    try:
        data = ''
        with open(file_name) as f:
            data = f.readlines()

        part_one(data)
    except FileNotFoundError:
        print(f'{file_name} not found')
