import re

def parse():
    data = open("Day04.txt", "r")
    return list(data)

def part1(data):
    overlaps = 0
    for row in data:
        match = re.match(r"(\d*)-(\d*),(\d*)-(\d*)", row.strip())
        a, b, c, d = map(int,match.groups())
        if a <= c and b >= d:
            overlaps += 1
        elif a >= c and b <= d:
            overlaps += 1
    return overlaps

def part2(data):
    overlaps = 0
    for row in data:
        match = re.match(r"(\d*)-(\d*),(\d*)-(\d*)", row.strip())
        a, b, c, d = map(int,match.groups())
        if a <= c <= b:
            overlaps += 1
        elif a <= d <= b:
            overlaps += 1
        elif c <= a <= d:
            overlaps += 1
        elif c <= b <= d:
            overlaps += 1
    return overlaps


if __name__ == '__main__':
    data = parse()
#     data = """2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8""".split("\n")

    print(f"Part 1 - {part1(data)}")
    print(f"Part 2 - {part2(data)}")