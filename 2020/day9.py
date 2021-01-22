import src  # My utility functions

NUMBERS = src.read(ints=True)
PRE = 25


def first_error(numbers, pre):
    for i, num in enumerate(numbers[pre:]):
        prev = numbers[i:i+25]
        if not any((num - p in prev) for p in prev):
            return num
    raise EOFError("End of list reached without breaking the rule.")


def adds_to(value, numbers):
    for i, num in enumerate(numbers):
        total = 0
        summands = []
        while total < value:
            total += numbers[i]
            summands.append(numbers[i])
            i += 1
        if total == value:
            return min(summands) + max(summands)
    raise EOFError("End of list reached without summing to the value.")


def main(numbers=None, pre=PRE):
    numbers = numbers or NUMBERS

    print("Part One:")
    first = first_error(numbers, pre)
    print(f"The first faulty number is {first}.")

    print("\nPart Two:")
    key = adds_to(first, numbers)
    print(f"The encryption weakness is {key}.")
    src.clip(key)


if __name__ == '__main__':
    main()
