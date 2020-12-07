import re
from typing import DefaultDict
from collections import defaultdict

EXAMPLE = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

PATTERN = re.compile(r"^(\S+ \S+) bags contain (.*)$")
CHILD_RE = re.compile(r"(\d+) (\S+ \S+)")


def day7a():
    with open("a.input.txt", "r") as f:
        lines = f.read().splitlines()

    bagMap = defaultdict(list)
    for line in lines:
        match = PATTERN.match(line)
        assert match
        parent = match[1]
        contents = [
            (color, int(quantity)) for quantity, color in CHILD_RE.findall(match[2])
        ]
        for color, _ in contents:
            bagMap[color].append(parent)

    totalColor = set()
    stack = bagMap["shiny gold"]

    while stack:
        color = stack.pop()
        if color not in totalColor:
            totalColor.add(color)
            stack.extend(bagMap[color])

    print(len(totalColor))


def day7b():
    with open("a.input.txt", "r") as f:
        lines = f.read().splitlines()

    bagMap: dict[str, list[tuple[str, int]]] = {}
    for line in lines:
        match = PATTERN.match(line)
        assert match
        parent = match[1]
        contents: list[tuple[str, int]] = [
            (color, int(quantity)) for quantity, color in CHILD_RE.findall(match[2])
        ]
        bagMap[parent] = contents

    queue: list[tuple[str, int]] = [("shiny gold", 1)]
    acc = 0
    while queue:
        color, quantity = queue.pop()
        acc += quantity
        for c, q in bagMap[color]:
            queue.append((c, q * quantity))
    acc -= 1
    print(acc)


def main():
    day7a()
    day7b()


if __name__ == "__main__":
    exit(main())
