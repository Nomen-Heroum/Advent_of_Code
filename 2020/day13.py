import src
import re

STRINGS = src.read()
EARLIEST = int(STRINGS[0])
IDS = [int(s) for s in re.findall(r'\d+', STRINGS[1])]
IDS_INDICES = []
for ind, num in enumerate(STRINGS[1].split(',')):
    try:
        IDS_INDICES.append((ind, int(num)))
    except ValueError:
        pass


def ans1(earliest, ids):
    waits = []
    for i in ids:
        waits.append([(i - (earliest % i)) % i, i])
    next_wait, next_id = min(waits)
    return next_wait * next_id


def ans2(ids_indices):
    product = 1
    index = 0
    for i, n in ids_indices:
        while (index + i) % n != 0:
            index += product
        product *= n
    return index


def main(earliest=EARLIEST, ids=None, ids_indices=None):
    ids = ids or IDS
    ids_indices = ids_indices or IDS_INDICES

    print("Part One:")
    ans = ans1(earliest, ids)
    print(f"The first answer is {ans}.")

    print("\nPart Two:")
    ans_2 = ans2(ids_indices)
    print(f"The second answer is {ans_2}!")
    src.copy(ans_2)


if __name__ == '__main__':
    main()
