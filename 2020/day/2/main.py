import collections

from typing import List
from dataclasses import dataclass


@dataclass
class CorporatePolicy:
    start: int
    end: int
    policy: str
    data: str
    counted: collections.Counter


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
            counted: collections.Counter = collections.Counter(data)
            arr.append(
                CorporatePolicy(
                    start=start, end=end, data=data, policy=policy, counted=counted
                )
            )
    return arr


def day2aExample(filename: str):
    items: List[CorporatePolicy] = parser(filename)
    valid: int = 0
    returnItem: int = -1
    for item in items:
        matchedPolicy: int = item.counted[item.policy]
        if matchedPolicy >= item.start and matchedPolicy <= item.end:
            valid += 1
    returnItem = valid

    return returnItem


def main():
    print(day2aExample("a.input.txt"))


if __name__ == "__main__":
    main()
