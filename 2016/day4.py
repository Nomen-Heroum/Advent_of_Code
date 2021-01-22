import src  # My utility functions
import re
from collections import defaultdict

ROOMS = src.read()


def id_sum(rooms: list):
    total = 0
    real_rooms = []
    for room in rooms:
        name, sector, checksum = re.findall(r'([\w-]+)-(\d+)\[(\w+)]', room)[0]
        letters = name.replace('-', '')
        occurences = defaultdict(int)
        for char in letters:
            occurences[char] += 1
        check = ''.join(sorted(occurences.keys(), key=lambda c: (-occurences[c], c))[:5])
        if check == checksum:
            sector = int(sector)
            total += sector
            real_rooms.append((name, sector))
    return total, sorted(real_rooms, key=lambda r: r[1])


def decrypt_rooms(real_rooms: list):
    with open('day4output.txt', 'w') as f:
        for room in real_rooms:
            name, sector = room
            shift = sector % 26
            f.write(f"Sector {sector}: ")
            for char in name:
                if char == '-':
                    f.write(' ')
                else:
                    f.write(chr((ord(char) - 97 + shift) % 26 + 97))
            f.write('\n')


def main(rooms=ROOMS):
    print("Part One:")
    ans1, real_rooms = id_sum(rooms)
    print(f"The sum of real room IDs is {ans1}.")

    print("\nPart Two:")
    decrypt_rooms(real_rooms)
    print("Room names written out to day4output.txt.")


if __name__ == '__main__':
    main()
