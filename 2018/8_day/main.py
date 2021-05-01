from __future__ import annotations
from functools import lru_cache
from dataclasses import dataclass


class Node:
    def __init__(self, num_children, num_metadata):
        self.num_children = num_children
        self.num_metadata = num_metadata
        self.nodes = []
        self.metadata = []

    def __repr__(self):
        return f'Node {self.num_children} {self.num_metadata} {self.nodes} {self.metadata}'

def parse_input(input: list[str]):
    num_children = int(input[0])
    num_metadata = int(input[1])
    node = Node(num_children, num_metadata)
    remaining_input = input[2:]
    while num_children > 0:
        (remaining_input,child) = parse_input(remaining_input)
        node.nodes.append(child)
        num_children -= 1

    while num_metadata > 0:
        metadata = int(remaining_input[0])
        node.metadata.append(metadata)
        remaining_input = remaining_input[1:]
        num_metadata -= 1

    return (remaining_input, node)


def sum_metadata(node: Node) -> int:
    total = 0
    nodes = [node]
    while len(nodes) > 0:
        current_node = nodes[0]
        nodes = nodes[1:]
        for child in current_node.nodes:
            nodes.append(child)
        total += sum(current_node.metadata)

    return total


@lru_cache
def sum_metadata_two(node: Node) -> int:
    num_children = node.num_children
    if num_children == 0:
        return sum(node.metadata)

    total = 0
    for index in node.metadata:
        if index > num_children:
            continue
        total += sum_metadata_two(node.nodes[index - 1])

    return total




def part_one(input: list[str]): 
    (_, node) = parse_input(input)
    total_metadata = sum_metadata(node)
    print(total_metadata)


def part_two(input: list[str]):
    (_, node) = parse_input(input)
    total_metadata = sum_metadata_two(node)
    print(total_metadata)


if __name__ == '__main__':
    file_name = 'input.txt'
    input = ''
    try:
        with open(file_name) as f:
            input = f.readlines()
        part_two(input[0].replace('\n', '').split(' '))
    except FileNotFoundError:
        print(f'can not find file {file_name}')
