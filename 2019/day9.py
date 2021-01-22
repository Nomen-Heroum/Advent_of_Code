import src  # My utility functions

INTCODE = src.read(',', ints=True)


def main(intcode=INTCODE):
    cpu = src.IntCodeCPU()
    print("Part One:")
    output = cpu.execute(intcode, 1)
    assert len(output) == 1, f"Some opcodes have malfunctioned: {output[:-1]}"
    ans1, = output  # 2457252183
    print(f"The BOOST keycode produced is {ans1}.")

    print("\nPart Two:")
    ans2, = cpu.execute(intcode, 2)  # 70634
    print(f"The coordinates of the distress signal are {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
