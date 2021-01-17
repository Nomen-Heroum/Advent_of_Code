import src
import re

STRINGS = src.read()


def find_clay(strings):
    clay = set()
    for s in strings:
        fixed = s[0]
        a, b, c = [int(n) for n in re.findall(r'\d+', s)]
        if fixed == 'x':
            clay |= {a + y*1j for y in range(b, c + 1)}
        else:
            clay |= {x + a*1j for x in range(b, c + 1)}
    return clay


def flow(strings):
    print("Simulating water flow...\r", end='')

    clay = find_clay(strings)
    min_y = min(clay, key=lambda z: z.imag).imag
    max_y = max(clay, key=lambda z: z.imag).imag
    current = [500 + min_y*1j]
    still = set()
    wet = set()
    while current:
        pos = current.pop()
        wet.add(pos)
        down = pos + 1j
        occupied = clay | still
        if down in occupied:
            resting = True
            layer = {pos}
            for direction in (-1, 1):
                new = pos + direction
                while new not in occupied and new + 1j in occupied:
                    layer.add(new)
                    new += direction
                wet |= layer
                if not {new, new + 1j} & occupied:
                    resting = False
                    current.append(new)
            if resting:
                current.append(pos - 1j)
                still |= layer
        elif down not in wet and down.imag <= max_y:
            current.append(down)
    return len(wet), len(still)


def main(strings=STRINGS):
    ans1, ans2 = flow(strings)
    print("Part One:")
    print(f"There are {ans1} tiles the water can reach.")  # 35707

    print("\nPart Two:")
    print(f"After the water drains, there are {ans2} tiles of water left.")  # 29293
    src.copy(ans2)


if __name__ == '__main__':
    main()
