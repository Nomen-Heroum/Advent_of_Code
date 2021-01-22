import src  # My utility functions

INTCODE = src.read(',', ints=True)


def diagnose(cpu, intcode, user_input):
    output = cpu.execute(intcode, user_input)
    assert not any(output[:-1]), f"{sum(bool(n) for n in output[:-1])} out of " \
                                 f"{len(output) - 1} diagnostic tests failed."
    print(f"Diagnostic test with input {user_input} run successfully.")
    return output[-1]


def main(intcode=INTCODE):
    cpu = src.IntcodeCPU()
    print("Part One:")
    ans1 = diagnose(cpu, intcode, 1)  # 14522484
    print(f"The program produces diagnostic code {ans1}.")

    print("\nPart Two:")
    ans2 = diagnose(cpu, intcode, 5)  # 4655956
    print(f"The diagnostic code for system ID 5 is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
