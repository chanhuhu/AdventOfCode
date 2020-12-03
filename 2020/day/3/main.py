from typing import List
from functools import reduce


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def openfile(filename: str):
    with open(filename, "r") as f:
        lines: List[str] = [i for i in f.read().splitlines()]
    return lines


def solveA(f: str):
    count = 0
    lines = openfile(f)
    height = len(lines)
    width = len(lines[0])
    x, y = 0, 0
    dx, dy = 3, 1
    x += dx
    x %= width  # repeat map
    y += dy
    while y < height:
        try:
            if lines[y][x] == "#":
                count += 1
        except IndexError:
            continue

        x += dx
        x %= width
        y += dy
    return count


def solveB(f: str):
    accumulator: List[int] = []
    for dx, dy in slopes:
        count = 0
        lines = openfile(f)
        height = len(lines)
        width = len(lines[0])
        x, y = 0, 0
        _dx, _dy = dx, dy
        x += _dx
        x %= width  # repeat map
        y += _dy
        while y < height:
            try:
                if lines[y][x] == "#":
                    count += 1
            except IndexError:
                continue

            x += _dx
            x %= width
            y += _dy
        accumulator.append(count)
    return reduce(lambda x, y: x * y, accumulator)


def day3a_example():
    f = "a.input.example.txt"
    print(solveA(f))
    return 0


def day3a():
    f: str = "a.input.txt"
    print(solveA(f))
    return 0


def day3b_example():
    f = "a.input.example.txt"
    print(solveB(f))
    return 0


def day3b():
    f: str = "a.input.txt"
    print(solveB(f))
    return 0


def main():
    day3a_example()
    day3a()
    day3b_example()
    day3b()


if __name__ == "__main__":
    main()
