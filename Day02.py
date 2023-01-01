
def parse():
    data = open("Day02.txt", "r")
    return list(data)

def part1(data):
    
    result = {}
    result["A X"] = 3 + 1
    result["A Y"] = 6 + 2
    result["A Z"] = 0 + 3
    result["B X"] = 0 + 1
    result["B Y"] = 3 + 2
    result["B Z"] = 6 + 3
    result["C X"] = 6 + 1
    result["C Y"] = 0 + 2
    result["C Z"] = 3 + 3
    
    game_sum = 0
    for row in data:
        game_sum += result[row.strip()]

    return game_sum


def part2(data):
    
    result = {}
    result["A X"] = 0 + 3
    result["A Y"] = 3 + 1
    result["A Z"] = 6 + 2
    result["B X"] = 0 + 1
    result["B Y"] = 3 + 2
    result["B Z"] = 6 + 3
    result["C X"] = 0 + 2
    result["C Y"] = 3 + 3
    result["C Z"] = 6 + 1
    
    game_sum = 0
    for row in data:
        game_sum += result[row.strip()]

    return game_sum

if __name__ == '__main__':
    data = parse()
    print(f"Part 1 - {part1(data)}")
    print(f"Part 2 - {part2(data)}")