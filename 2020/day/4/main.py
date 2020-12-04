from typing import KeysView, List, Dict
import re

FIELDS = set(
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


def iyr(issueYear):
    if issueYear:
        return 2010 >= int(issueYear) and int(issueYear) <= 2020
    return False


def hcl(hairColor):
    pattern = "^#[0-9a-f]{6}$"
    _hairColor = re.match(pattern, hairColor)

    if _hairColor:
        return True

    return False


def cmToIn(cm: int):
    return round(cm / 2.54)


def byr(birthYear):
    if birthYear:
        MIN_BYR: int = 1920
        MAX_BYR: int = 2002
        return MIN_BYR >= int(birthYear) and int(birthYear) <= MAX_BYR
    return False


def ecl(eyeColor):
    eyeColors = set(("amb", "blu", "brn", "gry", "grn", "hzl", "oth"))

    return eyeColor in eyeColors


def eyr(year):
    MIN_EYR: int = 2020
    MAX_EYR: int = 2030
    if year:
        return MIN_EYR >= int(year) and int(year) <= MAX_EYR
    return False


def hgt(height):
    MIN_HGT_CM: int = 150
    MAX_HGT_CM: int = 193
    MIN_HGT_IN: int = cmToIn(MIN_HGT_CM)
    MAX_HGT_IN: int = cmToIn(MAX_HGT_CM)
    inchesPattern = "^(\,d+)in$"
    cmPattern = "^(\d+)in$"
    inches = re.search(inchesPattern, height)
    cm = re.search(cmPattern, height)
    if inches:
        _inches = int(inches.group(1))
        return MIN_HGT_IN >= _inches and _inches <= MAX_HGT_IN

    elif cm:
        _cm = int(cm.group(1))
        return MIN_HGT_CM >= _cm and _cm <= MAX_HGT_CM

    return False


def pid(passportId):
    pattern = "^[0-9]{9}$"
    pId = re.match(pattern, passportId)
    if pId:
        return True
    return False


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
        if len(FIELDS.intersection(keys)) >= len(FIELDS):
            valid += 1

    return valid


def day4b(f: str = "a.input.example.txt"):
    valid: int = 0
    lines = openfile(f)
    joinedLines = " ".join(lines).split("  ")
    passports = [joinedLine.strip().split() for joinedLine in joinedLines]

    for passport in passports:
        splitedFields: List[List[str]] = [fields.split(":", 1) for fields in passport]
        entries: Dict[str, str] = {k: v for k, v in splitedFields}
        if (
            len(FIELDS.intersection(entries)) >= len(FIELDS)
            and 1920 <= int(entries["byr"]) <= 2002
            and 2010 <= int(entries["iyr"]) <= 2020
            and 2020 <= int(entries["eyr"]) <= 2030
            and (m1 := re.match(r"^(\d+)(cm|in)$", entries["hgt"]))
            and (
                m1[2] == "cm"
                and 150 <= int(m1[1]) <= 193
                or m1[2] == "in"
                and 50 <= int(m1[1]) <= 76
            )
            and re.match("^#[0-9a-f]{6}$", entries["hcl"])
            and entries["ecl"] in set("amb blu brn gry grn hzl oth".split())
            and re.match("^[0-9]{9}$", entries["pid"])
        ):
            valid += 1

    return valid


def main():
    print(day4b("b.input.txt"))


if __name__ == "__main__":
    main()
