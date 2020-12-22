import src
import re

STRINGS = src.read(5)


def is_nice(string):
    vowels = len(re.findall(r"[aeiou]", string))
    double = re.search(r"(.)\1", string)
    forbidden = re.search(r"ab|cd|pq|xy", string)
    if vowels >= 3 and double and not forbidden:
        return True
    return False


def is_nice2(string):
    doublepair = re.search(r"(..).*\1", string)
    repeatbetween = re.search(r"(.).\1", string)
    if doublepair and repeatbetween:
        return True
    return False


def count_nice(strings=STRINGS, nice=is_nice):
    santas_list = [nice(s) for s in strings]
    nice_amount = santas_list.count(True)
    print(f"{nice_amount} out of {len(strings)} strings are nice.")
    return nice_amount


src.copy(count_nice())
src.copy(count_nice(nice=is_nice2))



