import src
import re
from statistics import mode

STRING = src.read(split='\n\n')[0]


def bottom_program(string: str):
    program = string.split()[0]
    while True:
        mo = re.search(r'(\w+)[^\n]*->[^\n]*'+program, string)
        if not mo:
            return program
        program = mo[1]


def correct_weight(string: str, bottom: str):
    strings = string.splitlines()
    prog_dict = {}
    for s in strings:
        if '->' in s:
            program, weight, children = re.findall('(\w+) \((\d+)\) -> (.*)', s)[0]
            children = children.split(', ')
        else:
            program, weight = re.findall('(\w+) \((\d+)\)', s)[0]
            children = []
        prog_dict[program] = int(weight), children

    weights = {}

    def total_weight(prog):
        if prog in weights:
            return weights[prog]
        else:
            wgt, chl = prog_dict[prog]
            total = wgt + sum(total_weight(c) for c in chl)
            weights[prog] = total
            return total

    total_weight(bottom)  # Populate the dictionary of total weights

    def find_deviant(prog, prev):
        wgt, chl = prog_dict[prog]
        if len(chl) < 3:
            raise ValueError("Expected more children.")
        wts = [weights[c] for c in chl]
        common = mode(wts)
        for c in chl:
            if weights[c] != common:
                return find_deviant(c, common)
        return prog_dict[prog][0] + prev - weights[prog]

    return find_deviant(bottom, 0)


def main(string=STRING):
    print("Part One:")
    ans1 = bottom_program(string)  # azqje
    print(f"The bottom program is {ans1}.")

    print("\nPart Two:")
    ans2 = correct_weight(string, ans1)  # 646
    print(f"The faulty weight should be {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
