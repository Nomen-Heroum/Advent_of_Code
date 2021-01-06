import src
import functools
import operator

LENGTHS = [int(n) for n in src.read(',')]
STRING = src.read()[0]


def knot(lengths, version=1, size=256):
    if isinstance(lengths, str):
        lengths = [ord(c) for c in lengths] + [17, 31, 73, 47, 23]

    lst = list(range(size))
    first_pos = 0  # Keep track of the position of the first element when we rotate the list
    skip_size = 0

    repetitions = 1 if version == 1 else 64
    for _ in range(repetitions):
        for length in lengths:
            lst[:length] = lst[:length][::-1]
            rotation = (length + skip_size) % size
            lst = lst[rotation:] + lst[:rotation]  # Rotate the list
            first_pos -= rotation
            skip_size += 1
    first_pos %= size
    lst = lst[first_pos:] + lst[:first_pos]  # Put the first element back in front
    if version == 1:
        return lst[0] * lst[1]

    blocks = (lst[i:i + 16] for i in range(0, size, 16))
    dense_hash = [functools.reduce(operator.xor, b) for b in blocks]
    knot_hash = ''
    for n in dense_hash:
        knot_hash += hex(n)[-2:].replace('x', '0')
    return knot_hash


def main(lengths=None, string=STRING):
    lengths = lengths or LENGTHS

    print("Part One:")
    ans1 = knot(lengths)  # 3770
    print(f"The product of the first two numbers is {ans1}.")

    print("\nPart Two:")
    ans2 = knot(string, version=2)  # a9d0e68649d0174c8756a59ba21d4dc6
    print(f"The Knot Hash of my input is {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
