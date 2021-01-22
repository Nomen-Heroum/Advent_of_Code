import src  # My utility functions

NUMBERS = [19, 20, 14, 0, 9, 1]


def play(numbers, end):
    print(f"The elves are playing...\r", end='')
    dictionary = {k: i+1 for i, k in enumerate(numbers[:-1])}
    last = numbers[-1]
    for i in range(len(numbers), end):
        if last in dictionary:
            newlast = i - dictionary[last]
        else:
            newlast = 0
        dictionary[last] = i
        last = newlast
    return last


def main(numbers=None):
    numbers = numbers or NUMBERS

    print("Part One:")
    ans1 = play(numbers, 2020)  # 1325
    print(f"The 2020th number spoken is {ans1}.")

    print("\nPart Two:")
    ans2 = play(numbers, 30_000_000)  # 59006
    print(f"The 30,000,000th number spoken is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
