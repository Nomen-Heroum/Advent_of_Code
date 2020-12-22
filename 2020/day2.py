import src
import re

strings = src.read(2)

i = 0
for s in strings:
    lower, upper, char, pw = re.split('-| |: ', s)
    if int(lower) <= pw.count(char) <= int(upper):
        i += 1

print(f"There are {i} valid passwords out of a total of {len(strings)}.")

# Part Two
print("\n--- Part Two ---")

i = 0
for s in strings:
    pos1, pos2, char, pw = re.split('-| |: ', s)
    if (pw[int(pos1) - 1] == char) ^ (pw[int(pos2) - 1] == char):
        i += 1

print(f"There are {i} valid passwords out of a total of {len(strings)}.")