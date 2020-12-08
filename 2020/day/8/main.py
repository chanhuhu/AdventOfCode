class Instruction:
    def __init__(self):
        self.visited = set()
        self.acc = 0
        self.ptr = 0

    def execute(self, instruction: tuple[str, int]):
        op, val = instruction
        if op == "acc":
            self.ptr += 1
            self.acc += val
        elif op == "jmp":
            self.ptr += val
        elif op == "nop":
            self.ptr += 1
        else:
            raise NotImplementedError(self.visited)

    def run(self, instructions: list[tuple[str, int]]):

        while self.ptr not in self.visited and self.ptr < len(instructions):
            self.visited.add(self.ptr)
            self.execute(instructions[self.ptr])

            if self.ptr == len(instructions):
                return self.acc

    @staticmethod
    def switchOperation(op: str) -> str:
        return "jmp" if op == "nop" else "nop"

    def fixError(self, instructions: list[tuple[str, int]]):
        for idx, (op, val) in enumerate(instructions):
            if op in {"jmp", "nop"}:
                code = instructions.copy()
                code[idx] = (self.switchOperation(op), val)
                self.run(code)


def getInput(example: bool = False) -> list[tuple[str, int]]:
    if not example:
        with open("a.input.txt", "r") as f:
            code = [
                (op, int(val))
                for op, val in (line.split() for line in f.read().splitlines())
            ]
    else:
        code = [
            (op, int(val))
            for op, val in (line.split() for line in EXAMPLE.splitlines())
        ]
    return code


def day8a():
    code = getInput()
    instruction = Instruction()
    instruction.run(code)
    print(f"Part 1: {instruction.acc}")


EXAMPLE = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


def day8b():
    code = getInput(example=True)
    instruction = Instruction()
    instruction.fixError(code)


def main():
    # day8a()
    day8b()


if __name__ == "__main__":
    exit(main())
