import src  # My utility functions
from collections import deque
import string

STRINGS = src.read(',')


def dance(strings, size=16):
    """Separates the instructions into positional and named instructions. These commute with each other, so we can
    store them separately."""
    assert size <= 26, f"Expected 'size' of at most 26, got {size}"

    start = string.ascii_lowercase[:size]
    positions = deque(range(size))
    mask = start
    for s in strings:
        instruction = s[0]
        if instruction == 's':  # Spin, works on the positions
            positions.rotate(int(s[1:]))
        elif instruction == 'x':  # Exchange, works on the positions
            a, b = [int(n) for n in s[1:].split('/')]
            positions[a], positions[b] = positions[b], positions[a]
        else:  # Partner, works on the mask
            a, b = s[1:].split('/')
            mask = mask.translate(str.maketrans(a+b, b+a))
    return mask, list(positions)


def multiple_dances(mask: str, positions: list, repetitions: int, start=string.ascii_lowercase[:16]):
    current = start
    while repetitions:  # Scan all bits in repetitions right to left
        translation = str.maketrans(start, mask)
        if repetitions & 1:  # Current bit is 1
            masked = current.translate(translation)  # Apply the mask to the current string
            current = ''.join(masked[i] for i in positions)  # Shuffle according to positions
        mask = mask.translate(translation)
        positions = [positions[i] for i in positions]
        repetitions >>= 1  # Move on to the next bit
    return current


def main(strings=STRINGS):
    print("Part One:")
    mask, positions = dance(strings)
    ans1 = ''.join(mask[i] for i in positions)  # Shuffle the mask by the positions
    print(f"After dancing, the order is {ans1}.")  # jkmflcgpdbonihea

    print("\nPart Two:")
    ans2 = multiple_dances(mask, positions, 1000_000_000)  # ajcdefghpkblmion
    print(f"After a billion dances, the order is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
