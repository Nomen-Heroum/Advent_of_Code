import src
from collections import defaultdict

STRINGS = src.read(6)


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
    src.one()
    ans1 = error_correct(strings)
    print(f"The error-corrected message is {ans1}.")

    src.two()
    ans2 = error_correct(strings, version=2)
    print(f"Just kidding, it's actually {ans2}")
    src.copy(ans2)


if __name__ == '__main__':
    main()