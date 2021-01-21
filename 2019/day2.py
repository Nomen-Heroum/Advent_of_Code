import src

INTCODE = src.read(',', ints=True)


def main(intcode=INTCODE):
    cpu = src.IntCodeCPU()
    print("Part One:")
    intcode[1] = 12
    intcode[2] = 2
    cpu.execute(intcode)
    ans1 = cpu.memory[0]  # 2894520
    print(f"After the program halts, position 0 has a value of {ans1}.")

    print("\nPart Two:")
    ans2 = 0
    for noun in range(100):
        for verb in range(100):
            intcode[1] = noun
            intcode[2] = verb
            cpu.execute(intcode)
            if cpu.memory[0] == 1969_07_20:  # Date of the first moon landing!
                ans2 = 100 * noun + verb  # 9342
                break
    print(f"100 * noun + verb = {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
