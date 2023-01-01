def parse():
    with open("Day01.txt", "r") as data:
        data_list = [d.strip() for d in data]
        elf = 0
        elf_dict = {}
        for d in data_list:
            if d == '':
                elf += 1
            else:
                if elf not in elf_dict.keys():
                    elf_dict[elf] = 0
                elf_dict[elf] += int(d)

    return elf_dict

def part1(elf_dict):    
    return max(elf_dict.values())

def part2(elf_dict):
    elf_values = sorted(elf_dict.values(), reverse=True)
    return sum(elf_values[0:3])


if __name__ == '__main__':
    elf_dict = parse()
    print(f"part 1 - {part1(elf_dict)}")
    print(f"part 2 - {part2(elf_dict)}")