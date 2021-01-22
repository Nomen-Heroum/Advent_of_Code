import src  # My utility functions

DRIFTS = src.read(ints=True)


def first_repetition(drifts):
    frequency = 0
    seen = {0}
    while True:
        for n in drifts:
            frequency += n
            if frequency in seen:
                return frequency
            seen.add(frequency)


def main():
    print("Part One:")
    ans1 = sum(DRIFTS)  # 500
    print(f"The resulting frequency is {ans1}.")

    print("\nPart Two:")
    ans2 = first_repetition(DRIFTS)  # 709
    print(f"The first frequency reached twice is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
