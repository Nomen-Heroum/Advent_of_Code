import src
import itertools
import hashlib
import re

SALT = 'ihaygndm'


def find_otp(salt, version=1):
    print("Working...\r", end='')
    lowest = 0
    potential_keys = {}
    key_indices = []

    def encode(string):
        return hashlib.md5(string.encode('utf-8')).hexdigest()

    for i in itertools.count():
        hash_input = salt + str(i)
        hexa = encode(hash_input) if version == 1 else src.repeat(encode, hash_input, 2017)
        mo = re.search(r'(.)\1\1', hexa)
        if mo:
            if not potential_keys:
                lowest = i
            potential_keys[i] = [mo[1], hexa, False]

            for index, (char, _hex, _bool) in potential_keys.items():
                if re.search(char*5, hexa) and index != i:
                    potential_keys[index][-1] = True

        if potential_keys and i == lowest + 1000:
            if potential_keys[lowest][-1]:
                key_indices.append(lowest)
                if len(key_indices) == 64:
                    return lowest
            del potential_keys[lowest]
            lowest = min(potential_keys) if potential_keys else 0


def main(salt=SALT):
    print("Part One:")
    ans1 = find_otp(salt)
    print(f"Index {ans1} gives the 64th key.")

    print("\nPart Two:")
    ans2 = find_otp(salt, version=2)
    print(f"With key stretching, this index is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
