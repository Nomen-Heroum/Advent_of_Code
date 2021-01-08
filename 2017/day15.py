import src

A_START = 703
B_START = 516


def count_matches(a_start, b_start, iterations):
    print("Counting...\r", end='')
    matches = 0
    a = a_start
    b = b_start
    last_bits = (1 << 16) - 1
    for i in range(1, iterations + 1):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
        if a & last_bits == b & last_bits:
            matches += 1
    return matches


def count_matches_2(a_start, b_start, iterations):
    """Separated out from count_matches to prevent slowdown."""
    print("Counting...\r", end='')
    matches = 0
    a = a_start
    b = b_start
    last_bits = (1 << 16) - 1
    for i in range(1, iterations + 1):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
        while a & 0b11:
            a = (a * 16807) % 2147483647
        while b & 0b111:
            b = (b * 48271) % 2147483647
        if a & last_bits == b & last_bits:
            matches += 1
    return matches


def main(a_start=A_START, b_start=B_START):
    print("Part One:")
    ans1 = count_matches(a_start, b_start, 40_000_000)  # 594
    print(f"The judge's final count is {ans1}.")

    print("\nPart Two:")
    ans2 = count_matches_2(a_start, b_start, 5_000_000)  # 328
    print(f"The count is now {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
