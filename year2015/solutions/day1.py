from utils.files import read_file


def part_1(input: str) -> int:
    content = read_file(input)
    floor = 0
    for instruction in content:
        if instruction == '(':
            floor += 1
        elif instruction == ')':
            floor -= 1 
    return floor


if __name__ == "__main__":
    filename = "year2015/inputs/day1.txt"
    result = part_1(filename)
    print(result)