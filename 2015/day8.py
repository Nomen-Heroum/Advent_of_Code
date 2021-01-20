import src
import re

STRINGS = src.read()
TOTAL_CHARS = sum(len(s) for s in STRINGS)


def count_mem_chars(strings=STRINGS):
    no_quotes = (s.strip('"') for s in strings)
    short = (re.sub(r'\\\\|\\"|\\x[0-9a-f]{2}', '#', s) for s in no_quotes)
    return sum(len(s) for s in short)


def count_rep_chars(strings=STRINGS):
    reps = (re.sub(r'(["\\])', '##', s) for s in strings)
    return sum(len(s) + 2 for s in reps)


def main():
    print("Part One:")
    mem_chars = count_mem_chars()
    diff = TOTAL_CHARS - mem_chars
    print(f"Code characters: {TOTAL_CHARS}.\n"
          f"Memory characters: {mem_chars}.\n"
          f"Difference: {diff}.")

    print("\nPart Two:")
    rep_chars = count_rep_chars()
    diff2 = rep_chars - TOTAL_CHARS
    print(f"Code characters: {TOTAL_CHARS}.\n"
          f"Representation characters: {rep_chars}.\n"
          f"Difference: {diff2}.")
    src.clip(diff2)


if __name__ == '__main__':
    main()
