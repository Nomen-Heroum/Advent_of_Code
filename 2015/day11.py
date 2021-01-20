import src
import re

PASSWORD = 'vzbxkghb'


def iterate(password, i=-1):
    pw_ords = [ord(c) for c in password]
    if pw_ords[i] in [104, 107, 110]:
        pw_ords[i] += 2
    elif 97 <= pw_ords[i] < 122:
        pw_ords[i] += 1
    elif pw_ords[i] == 122:
        pw_ords[i] = 97
        newpw = ''.join(chr(o) for o in pw_ords)
        return iterate(newpw, i=i-1)
    newpw = ''.join(chr(o) for o in pw_ords)
    return newpw


def check(password):
    pw_ords = [ord(c) for c in password]
    conds = [
        any((pw_ords[i + 1] == o + 1 and pw_ords[i + 2] == o + 2) for i, o in enumerate(pw_ords[:-2])),
        not any(o in [105, 108, 111] for o in pw_ords),
        len(re.findall(r'(.)\1', password)) >= 2
    ]
    return True if all(conds) else False


def find(password):
    while not check(password):
        password = iterate(password)
    return password


def main(password=PASSWORD):
    print("Part One:")
    final = find(password)
    print(f"The final password is {final}.")

    print("\nPart Two:")
    next_pw = find(iterate(final))
    print(f"Santa's next password is {next_pw}.")
    src.clip(next_pw)


if __name__ == '__main__':
    main()
