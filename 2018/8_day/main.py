from __future__ import annotations
from dataclasses import dataclass


class Node:
    def __init__(self, num_children, num_metadata):
        self.num_children = num_children
        self.num_metadata = num_metadata
        self.nodes = []

    def add_node(node):
        self.nodes.append(node)

def parse_input(input: list[str]):
    num_children = int(input[0])
    num_metadata = int(input[1])
    node = Node(num_children, num_metadata)


def part_one(input: list[str]): 
    print(input)


if __name__ == '__main__':
    file_name = 'sample.txt'
    input = ''
    try:
        with open(file_name) as f:
            input = f.readlines()
        part_one(input)
    except FileNotFoundError:
        print(f'can not find file {file_name}')
