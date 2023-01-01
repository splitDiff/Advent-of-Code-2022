def parse():
    data = open("Day06.txt", "r")
    return data.read()



def part1(data):
    for i in range(len(data)):
        if i < 3:
            continue
        if len(set(data[i-3:i+1]))==4:
            return i+1


def part2(data):
    for i in range(len(data)):
        if i < 13:
            continue
        if len(set(data[i-13:i+1]))==14:
            return i+1

if __name__ == '__main__':
    data = parse()

    assert(part1("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7)
    assert(part1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5)
    assert(part1("nppdvjthqldpwncqszvftbrmjlhg") == 6)
    assert(part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10)
    assert(part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11)
    
    print(f"Part 1 - {part1(data)}")

    assert(part2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19)
    assert(part2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23)
    assert(part2("nppdvjthqldpwncqszvftbrmjlhg") == 23)
    assert(part2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29)
    assert(part2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26)
    
    print(f"Part 2 - {part2(data)}")