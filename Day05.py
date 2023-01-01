import re
from dataclasses import dataclass
from collections import deque


@dataclass
class move:
    qty: int
    from_col: int
    to_col: int

def parse():
    data = open("Day05.txt", "r")
    return list(data)


def get_cols(data):
    stacks = []
    cols = {}
    for row in data:
        if row[0:3] == ' 1 ':
            break
        stacks.append(row.strip('\n'))
    for row in stacks:
        for i in range(1, len(row), 4):
            col_name = (i+3)//4
            if row[i] == ' ':
                continue
            if col_name not in cols.keys():
                cols[col_name] = deque(row[i])
            else:
                cols[col_name].append(row[i])
    return cols


def get_moves(data):
    instructions = []
    for row in data:
        if row[0:5] != 'move ':
            continue
        instructions.append(row.strip('\n'))
    moves = []
    for row in instructions:
        match = re.match(r"move (\d*) from (\d*) to (\d*)", row)
        qty = int(match.groups()[0])
        from_col = int(match.groups()[1])
        to_col = int(match.groups()[2])

        moves.append(move(qty,from_col,to_col))
    return moves

def make_moves(cols:list[deque], moves:list[move]):
    for move in moves:
        for i in range(move.qty):
            item = cols[move.from_col].popleft()
            cols[move.to_col].appendleft(item)
    return cols

def make_moves_2(cols:dict[int:deque], moves:list[move]):
    for move in moves:
        items = deque()
        for i in range(move.qty):
            items.append(cols[move.from_col].popleft())
        for i in range(move.qty):
            cols[move.to_col].appendleft(items.pop())
    return cols


def get_results(cols:dict[int:deque]):
    result = []
    for i in sorted(cols.keys()):
        result.append(cols[i].popleft())
    return ''.join(result)

def part1(data):
    cols = get_cols(data)
    moves = get_moves(data)
    results = make_moves(cols,moves)
    return get_results(results)

def part2(data):
    cols = get_cols(data)
    moves = get_moves(data)
    results = make_moves_2(cols,moves)
    return get_results(results)

test_data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".split('\n')


if __name__ == '__main__':
    data = parse()
    # data = test_data
    print(f"Part 1 - {part1(data)}")
    print(f"Part 2 - {part2(data)}")