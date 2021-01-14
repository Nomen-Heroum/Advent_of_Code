import src
from collections import defaultdict

with open('Input/input13.txt') as file:  # Had to add extra spaces at the end of the input file
    STRINGS = file.read().splitlines()   # to prevent '\' from escaping newlines


def find_collisions(strings):
    directions = {'<': -1, '>': 1, '^': -1j, 'v': 1j}
    dct = defaultdict(set)
    minecarts = {}
    for y, string in enumerate(strings):
        for x, char in enumerate(string):
            pos = x + y*1j
            if char in ('<', '>', '^', 'v'):
                minecarts[pos] = directions[char], -1j  # Heading, next choice at intersection
            if char == '+':
                dct['intersections'].add(pos)
            elif char == '/':
                dct['left'].add(pos)  # Cart turns left if travelling horizontally
            elif char == '\\':
                dct['right'].add(pos)  # Horizontal cart turns right

    first_crash = None
    while len(minecarts) > 1:
        carts = sorted(minecarts.items(), key=lambda tup: (tup[0].imag, tup[0].real))  # Sort by y, then x
        for cart, (direction, choice) in carts:
            if cart not in minecarts:  # Another cart has already crashed into it
                continue
            del minecarts[cart]  # Remove old position

            if cart in dct['intersections']:
                direction *= choice  # Turn according to choice
                choice *= -1 if choice == 1j else 1j  # Update choice
            elif cart in dct['left']:
                direction *= -1j if direction.real else 1j
            elif cart in dct['right']:
                direction *= 1j if direction.real else -1j

            cart += direction  # Move cart
            if cart in minecarts:  # Collision
                if not first_crash:
                    first_crash = f"{int(cart.real)},{int(cart.imag)}"
                del minecarts[cart]
            else:
                minecarts[cart] = (direction, choice)
    last_cart = list(minecarts.keys())[0]
    return first_crash, f"{int(last_cart.real)},{int(last_cart.imag)}"


def main(strings=None):
    strings = strings or STRINGS

    ans1, ans2 = find_collisions(strings)
    print("Part One:")
    print(f"The first collision occurs at {ans1}.")  # 40,90

    print("\nPart Two:")
    print(f"After the last collision, the last cart is at {ans2}.")  # 106,22 is wrong
    src.copy(ans2)


if __name__ == '__main__':
    main()
