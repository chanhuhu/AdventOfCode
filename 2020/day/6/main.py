import sys
import collections

inputExample = """\
abc

a
b
c

ab
ac

a
a
a
a

b
"""


def day6a():
    cnt = 0
    try:
        f = sys.argv[1]
        with open(f, "r") as f:
            groups = f.read().split("\n\n")

        for group in groups:
            counter = collections.Counter(set(group) - {"\n"})
            cnt += sum(counter.values())

    except IndexError:
        groups = inputExample.split("\n\n")
        print(groups)
        for group in groups:
            counter = collections.Counter(set(group) - {"\n"})
            cnt += sum(counter.values())

    print(f"part a = {cnt}")


def day6b():
    cnt = 0
    try:
        f = sys.argv[1]
        with open(f, "r") as f:
            groups = f.read().split("\n\n")

        for group in groups:
            counter = collections.Counter(set(group) - {"\n"})
            answers = [set(x) for x in group.split("\n") if x != ""]
            counter = collections.Counter(answers[0].intersection(*answers[1:]))
            cnt += sum(counter.values())

    except IndexError:
        groups = inputExample.split("\n\n")
        for group in groups:
            counter = collections.Counter(set(group) - {"\n"})
            answers = [set(x) for x in group.split("\n") if x != ""]
            counter = collections.Counter(answers[0].intersection(*answers[1:]))
            cnt += sum(counter.values())

    print(f"part b = {cnt}")


def main():
    day6a()
    day6b()


if __name__ == "__main__":
    exit(main())
