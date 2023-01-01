def parse():
    data = open("Day03.txt", "r")
    return list(data)

def priority(char):
    char_ord = ord(char)
    if char_ord > 96:
        return char_ord - 96
    else:
        return char_ord - 38



def part1(data):
    total = 0
    for row in data:
        half_row = len(row)//2
        sec1 = set(row[0:half_row])
        sec2 = set(row[half_row:])
        total += priority((sec1&sec2).pop())

    return total

    ...
def part2(data):
    total = 0
    for i in range(0, len(data), 3):
        id = (set(data[i].strip()) & set(data[i+1].strip()) & set(data[i+2].strip())).pop()
        total += priority(id)
    return total



if __name__ == '__main__':
    data = parse()
#     data = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw""".split("\n")
    print(f"Part 1 - {part1(data)}")
    print(f"Part 2 - {part2(data)}")