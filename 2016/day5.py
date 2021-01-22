import src  # My utility functions
import itertools
import hashlib

DOOR_ID = 'ojvtpuvg'


def find_password(door_id, n=5, version=1):
    print("Searching for the password...\n"
          "________\r", end='')
    password = ['_'] * 8
    not_found = set(range(8))
    index = 0
    for i in itertools.count():
        hash_input = door_id + str(i)
        hexa = hashlib.md5(hash_input.encode('utf-8')).hexdigest()
        if hexa[:n] == n * '0':
            char = hexa[n]
            if version == 1:
                password[index] = char
                index += 1
            else:
                try:
                    pos = int(char)
                    if pos in not_found:
                        not_found.remove(pos)
                        password[pos] = hexa[n+1]
                except ValueError:
                    pass
            if '_' not in password:
                return ''.join(password)
            print(''.join(password)+'\r', end='')


def main(door_id=DOOR_ID):
    print("Part One:")
    ans1 = find_password(door_id)
    print(f"The password is {ans1}.")

    print("\nPart Two:")
    ans2 = find_password(door_id, version=2)
    print(f"The second password is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
