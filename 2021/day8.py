import src  # My utility functions
from collections import defaultdict

STRINGS = src.read()
DIGIT_LENGTHS = {2: 1,
                 3: 7,
                 4: 4,
                 7: 8}


def simple_digits(strings):
    count = 0
    for string in strings:
        count += sum(len(digit) in DIGIT_LENGTHS for digit in string.split()[-4:])
    return count


def determine_outputs(strings):
    total = 0
    for string in strings:
        patterns, output = string.split(' | ')
        patterns = [frozenset(p) for p in patterns.split()]  # Frozen set for hashing into a dict
        output = [frozenset(o) for o in output.split()]

        # Build a dict of pattern lengths
        lengths = defaultdict(list)
        for patt in patterns:
            lengths[len(patt)].append(patt)

        digits = {}
        # Fill in the simple digits
        for length, digit in DIGIT_LENGTHS.items():
            digits[digit] = lengths[length][0]

        # Deduce patterns of length 5
        for patt in lengths[5]:
            if digits[1] <= patt:
                digits[3] = patt
            elif len(digits[4] & patt) == 2:
                digits[2] = patt
            else:
                digits[5] = patt

        # Deduce patterns of length 6
        for patt in lengths[6]:
            if digits[4] <= patt:
                digits[9] = patt
            elif digits[1] <= patt:
                digits[0] = patt
            else:
                digits[6] = patt

        reverse_digits = {pattern: digit for digit, pattern in digits.items()}
        total += sum(reverse_digits[output[-i - 1]] * 10**i for i in range(4))

    return total


def main(strings=STRINGS):
    print("Part One:")
    ans1 = simple_digits(strings)  # 330
    print(f"The digits 1, 4, 7 and 8 appear {ans1} times in the output values.")

    print("\nPart Two:")
    ans2 = determine_outputs(strings)  # 1010472
    print(f"Adding up all the output values gives {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
