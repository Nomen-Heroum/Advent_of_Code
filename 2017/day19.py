import src
import string

PIPE = {}
with open('Input/input19.txt') as file:  # src.read() strips input, which we can't afford here
    for y, line in enumerate(file.read().splitlines()):
        for x, char in enumerate(line):
            if char != ' ':
                PIPE[x + y * 1j] = char
                if not y:
                    START = x


def gather_letters(pipe, start):
    position = start
    direction = 1j
    letters = ''
    steps = 0
    while True:
        position += direction
        steps += 1
        try:
            character = pipe[position]
            if character == '+':
                direction *= 1j
                if position + direction not in pipe:
                    direction *= -1
            elif character in string.ascii_letters:
                letters += character
        except KeyError:
            return letters, steps


def main(pipe=None, start=START):
    pipe = pipe or PIPE

    ans1, ans2 = gather_letters(pipe, start)
    print("Part One:")
    print(f"The letters encountered are {ans1}.")  # DWNBGECOMY

    print("\nPart Two:")
    print(f"The packet needs to go {ans2} steps.")  # 17228
    src.clip(ans2)


if __name__ == '__main__':
    main()
