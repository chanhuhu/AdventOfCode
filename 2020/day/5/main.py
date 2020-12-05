INPUT_EXAMPLE = "FBFBBFFRLR"


def day5a(filename: str = "a.input.txt"):
    maximum = 0
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            row = int(
                line[:7].replace("F", "0").replace("B", "1"), 2
            )  # parse binary number
            col = int(line[-3:].replace("L", "0").replace("R", "1"), 2)
            maximum = max(maximum, row * 8 + col)

    print(f"maximum seat ID is: {maximum}")


def day5b(filename: str = "b.input.txt"):
    listIDs: list[int] = []
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            row = int(
                line[:7].replace("F", "0").replace("B", "1"), 2
            )  # parse binary number
            col = int(line[-3:].replace("L", "0").replace("R", "1"), 2)
            id = row * 8 + col
            listIDs.append(id)
    expected_total = sum(range(min(listIDs), max(listIDs) + 1))
    total = sum([s for s in listIDs])
    print("solution for part 2:", expected_total - total)


def main():
    day5a()
    day5b()


if __name__ == "__main__":
    main()
