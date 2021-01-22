import src  # My utility functions
from collections import defaultdict

STRINGS = src.read()


def error_correct(strings, version=1):
    n = len(strings[0])
    message = ''
    ver = 1 if version == 1 else -1
    for i in range(n):
        chars = defaultdict(int)
        for s in strings:
            chars[s[i]] += 1
        message += max(chars, key=lambda c: ver * chars[c])
    return message


def main(strings=STRINGS):
    print("Part One:")
    ans1 = error_correct(strings)
    print(f"The error-corrected message is {ans1}.")

    print("\nPart Two:")
    ans2 = error_correct(strings, version=2)
    print(f"Just kidding, it's actually {ans2}")
    src.clip(ans2)


if __name__ == '__main__':
    main()
