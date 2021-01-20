import src

NUMBERS = [[int(n) for n in s.split()] for s in src.read()]


def checksum(numbers):
    return sum(max(row) - min(row) for row in numbers)


def sum_divisions(numbers):
    def find_quotient(row):
        for i, num1 in enumerate(row):
            candidates = (n for n in row[:i] + row[i+1:] if n <= num1)
            for num2 in candidates:
                quotient, remainder = divmod(num1, num2)
                if remainder == 0:
                    return quotient

    return sum(find_quotient(r) for r in numbers)


def main(numbers=None):
    numbers = numbers or NUMBERS

    print("Part One:")
    ans1 = checksum(numbers)  # 36766
    print(f"The checksum of this spreadsheet is {ans1}.")

    print("\nPart Two:")
    ans2 = sum_divisions(numbers)  # 16
    print(f"The sum of each even division is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
