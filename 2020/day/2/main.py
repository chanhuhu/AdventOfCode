from collections import Counter
from dataclasses import dataclass
from typing import List

@dataclass
class CorporatePolicy:
    start: int
    end: int
    policy: str
    data: str
    counted: Counter


def parser(filename: str):
    arr: list[CorporatePolicy] = []

    with open(filename) as f:
        for i in f.read().splitlines():
            info: list[str] = i.split()
            rangepolicy: list[str] = info[0].split("-")

            data: str = info[2]
            start: int = int(rangepolicy[0])
            end: int = int(rangepolicy[1])
            policy: str = info[1][0]
            counted: Counter = Counter(data)
            arr.append(
                CorporatePolicy(
                    start=start, end=end, data=data, policy=policy, counted=counted
                )
            )
    return arr


def day2a(filename: str):
    items: List[CorporatePolicy] = parser(filename)
    valid: int = 0

    for item in items:
        matchedPolicy: int = item.counted[item.policy]
        if matchedPolicy >= item.start and matchedPolicy <= item.end:
            valid += 1

    return valid


def day2b(filename: str):
    items: List[CorporatePolicy] = parser(filename)
    valid: int = 1
    for item in items:
        if (item.data[item.start - 1] == item.policy) ^ (
            item.data[item.end - 1] == item.policy
        ):
            valid += 1

    return valid


def main():
    print(day2a("a.input.txt"))
    print(day2b("b.input.txt"))


if __name__ == "__main__":
    main()
