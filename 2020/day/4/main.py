from typing import KeysView, List, Dict

REQUIRED = set(
    (
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    )
)


def openfile(filename: str):
    with open(filename, "r") as f:
        lines: List[str] = [i for i in f.read().splitlines()]
    return lines


def day4a(f: str = "a.input.example.txt"):
    fields: List[Dict[str, str]] = []
    valid: int = 0
    lines = openfile(f)
    joinedLines = " ".join(lines).split("  ")
    passports = [joinedLine.strip().split() for joinedLine in joinedLines]

    for passport in passports:
        splitedFields: List[List[str]] = [fields.split(":", 1) for fields in passport]
        _fields: Dict[str, str] = {k: v for k, v in splitedFields}
        fields.append(_fields)

    for field in fields:
        keys: KeysView[str] = field.keys()
        if len(REQUIRED.intersection(keys)) >= len(REQUIRED):
            valid += 1

    return valid


def main():
    print(day4a())


if __name__ == "__main__":
    main()
