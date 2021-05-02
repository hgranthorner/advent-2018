from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class Circle:
    marbles: list[int] = field(default_factory=lambda: [0])
    pos: int = 0
    players: dict[int, int] = field(default_factory=dict)
    current_player: int = 1

    def add_players(self, x: int):
        for i in range(1, x + 1):
            self.players[i] = 0

    def clockwise(self, x):
        self.pos = self.pos + x
        if self.pos >= len(self.marbles):
            self.pos = self.pos - len(self.marbles)

    def counter_clockwise(self, x):
        self.pos = self.pos - x
        if self.pos < 0:
            self.pos = self.pos + len(self.marbles)

    def insert(self, x):
        if self.pos == 0:
            self.marbles.append(x)
            self.pos = len(self.marbles) - 1
        else:
            self.marbles.insert(self.pos, x)

        self.current_player += 1
        if self.current_player > len(self.players):
            self.current_player = 1

    def take_from_circle(self):
        ps = self.players
        cp = self.current_player
        # first, take the requisite 23
        self.players[self.current_player] += 23

        # then, remove the current marble and reassign
        marble = self.marbles[self.pos]
        self.players[self.current_player] += marble
        del self.marbles[self.pos]

        self.current_player += 1
        if self.current_player > len(self.players):
            self.current_player = 1


def can_convert(x: str):
    try:
        int(x)
        return True
    except ValueError:
        return False

def parse_input(input: str):
    words = [int(x) for x in input.split(' ') if can_convert(x)]
    num_players = words[0]
    max_marble = words[1]
    circle = Circle()
    circle.add_players(num_players)
    for i in range(1, max_marble + 1):
        print(f'\n{i}: current player {circle.current_player}')
        if i % 23 == 0:
            circle.counter_clockwise(7)
            circle.take_from_circle()
            print(f'Current state: pos: {circle.pos}; score: {circle.players}')
            print(circle.marbles)
            continue
        circle.clockwise(2)
        circle.insert(i)
        print(f'Current state: pos: {circle.pos}; score: {circle.players}')
        print(circle.marbles)

    return circle

def part_one(input: str): 
    circle = parse_input(input)
    high_score = max(circle.players.values())
    print(high_score)


def part_two(input: str): pass

if __name__=='__main__':
    file_name = 'sample.txt'
    input = ''
    try:
        with open(file_name) as f:
            input = f.readline()
        part_one(input)
    except FileNotFoundError:
        print(f'can not find file {file_name}')
