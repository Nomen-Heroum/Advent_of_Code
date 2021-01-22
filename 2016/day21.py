import src  # My utility functions
import parse

PASSWORD = 'abcdefgh'  # Seriously?
PASSWORD_2 = 'fbgdceah'
STRINGS = src.read()
swap = parse.compile('swap {} {} with {} {}')
step = parse.compile('rotate {} {:d} step')
reverse = parse.compile('reverse positions {:d} through {:d}')
move = parse.compile('move position {:d} to position {:d}')


def scramble(password: str, strings: list):
    n = len(password)
    pw = list(password)
    for s in strings:
        if 'swap' in s:
            to_swap, x, _, y = swap.parse(s)
            if to_swap == 'position':
                x, y = int(x), int(y)
                pw[x], pw[y] = pw[y], pw[x]
            else:
                ix, iy = pw.index(x), pw.index(y)
                pw[ix], pw[iy] = y, x
        elif 'step' in s:
            direction, x = step.search(s)
            rotation = x if direction == 'left' else -x
            pw = pw[rotation:] + pw[:rotation]
        elif 'based' in s:
            x = s[-1]
            index = pw.index(x)
            rotation = (index + 1) % n if index < 4 else (index + 2) % n
            pw = pw[-rotation:] + pw[:-rotation]
        elif 'reverse' in s:
            x, y = reverse.parse(s)
            pw[x:y + 1] = pw[x:y + 1][::-1]
        elif 'move' in s:
            x, y = move.parse(s)
            pw.insert(y, pw.pop(x))
        else:
            raise ValueError("Unexpected instruction encountered.")
    return ''.join(pw)


unrotate = {0: 1, 1: 1, 2: 6, 3: 2, 4: 7, 5: 3, 6: 0, 7: 4}  # Reverse mapping for 'rotate based on'


def unscramble(password: str, strings: list):
    pw = list(password)
    strings.reverse()
    for s in strings:
        if 'swap' in s:
            to_swap, x, _, y = swap.parse(s)
            if to_swap == 'position':
                x, y = int(x), int(y)
                pw[x], pw[y] = pw[y], pw[x]
            else:
                ix, iy = pw.index(x), pw.index(y)
                pw[ix], pw[iy] = y, x
        elif 'step' in s:
            direction, x = step.search(s)
            rotation = x if direction == 'right' else -x
            pw = pw[rotation:] + pw[:rotation]
        elif 'based' in s:
            x = s[-1]
            index = pw.index(x)
            rotation = unrotate[index]
            pw = pw[rotation:] + pw[:rotation]
        elif 'reverse' in s:
            x, y = reverse.parse(s)
            pw[x:y + 1] = pw[x:y+1][::-1]
        elif 'move' in s:
            x, y = move.parse(s)
            pw.insert(x, pw.pop(y))
        else:
            raise ValueError("Unexpected instruction encountered.")
    return ''.join(pw)


def main(password=PASSWORD, strings=STRINGS, password_2=PASSWORD_2):
    print("Part One:")
    ans1 = scramble(password, strings)  # gfdhebac
    print(f"The result of scrambling {password} is {ans1}.")

    print("\nPart Two:")
    ans2 = unscramble(password_2, strings)  # dhaegfbc
    print(f"The unscrambled version of fbgdceah is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
