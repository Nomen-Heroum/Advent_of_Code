import src
from itertools import permutations

INTCODE = src.read(',', ints=True)


def try_phases(intcode, phases):
    max_signal = 0
    for sequence in permutations(phases):
        cpus = [src.IntCodeCPU(intcode, phase) for phase in sequence]
        signal = 0
        amp = 0
        while cpus[amp].running:
            cpus[amp].input.append(signal)
            signal, = cpus[amp].execute()
            amp += 1
            amp %= 5
        max_signal = max(max_signal, signal)
    return max_signal


def main(intcode=INTCODE):
    print("Part One:")
    ans1 = try_phases(intcode, range(5))
    print(f"The highest possible signal is {ans1}.")  # 75228

    print("\nPart Two:")
    ans2 = try_phases(intcode, range(5, 10))  # 79846026
    print(f"The highest signal with feedback is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
