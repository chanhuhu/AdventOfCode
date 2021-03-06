class VirtualMachine:
    def __init__(self):
        self.executed = set()
        self.accumulator = 0
        self.programCounter = 0

    def execute(self, instr: tuple[str, int]):
        op, val = instr
        if op == "acc":
            self.programCounter += 1
            self.accumulator += val
        elif op == "jmp":
            self.programCounter += val
        elif op == "nop":
            self.programCounter += 1
        else:
            raise NotImplementedError(self.executed)

    def run(self, instrs: list[tuple[str, int]]):

        while self.programCounter not in self.executed and self.programCounter < len(
            instrs
        ):
            self.executed.add(self.programCounter)
            self.execute(instrs[self.programCounter])


    def runAndFixError(self, instrs: list[tuple[str, int]]):
        for idx, (op, val) in enumerate(instrs):
            swap = {"jmp": "nop", "nop": "jmp"}
            if op in swap:
                opCode = instrs.copy()
                opCode[idx] = (swap[op], val)
                try:
                    self.run(opCode)
                except:
                    raise RuntimeError(self.executed)

            if self.programCounter == len(instrs):
                break
            else:
                RuntimeError(self.executed)


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
    v = VirtualMachine()
    v.run(code)
    print(f"Part 1: {v.accumulator}")


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
    instrs = getInput()
    v = VirtualMachine()
    v.runAndFixError(instrs)
    print(f"Part 2: {v.accumulator}")


def main():
    day8a()
    day8b()


if __name__ == "__main__":
    exit(main())
