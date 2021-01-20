import src
from collections import Counter

BOX_IDS = src.read()


def checksum(box_ids):
    two_count = 0
    three_count = 0
    for box_id in box_ids:
        letter_counts = Counter(box_id).values()
        two_count += 2 in letter_counts
        three_count += 3 in letter_counts
    return two_count * three_count


def common_letters(box_ids):
    id_length = len(box_ids[0])
    for i, id1 in enumerate(box_ids):
        for id2 in box_ids[i+1:]:
            if sum(id1[i] != id2[i] for i in range(id_length)) == 1:
                return ''.join(c for i, c in enumerate(id1) if id2[i] == c)


def main(box_ids=BOX_IDS):
    print("Part One:")
    ans1 = checksum(box_ids)  # 5681
    print(f"The checksum is {ans1}.")

    print("\nPart Two:")
    ans2 = common_letters(box_ids)  # uqyoeizfvmbistpkgnocjtwld
    print(f"The common letters between the two correct IDs are {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
