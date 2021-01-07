import src

PUBLIC_KEY_1 = 6930903
PUBLIC_KEY_2 = 19716708
MODULUS = 20201227


def find_encryption_key(public_key_1: int, public_key_2: int, modulus: int):
    num = 1
    loop_sizes = []
    for i in range(1, modulus+1):
        num = num*7 % modulus
        if num == public_key_1 or num == public_key_2:
            loop_sizes.append(i)
            if len(loop_sizes) == 2:
                break

    return pow(7, loop_sizes[0] * loop_sizes[1], modulus)


def main(public_key_1=PUBLIC_KEY_1, public_key_2=PUBLIC_KEY_2, modulus=MODULUS):
    print("Part One:")
    ans1 = find_encryption_key(public_key_1, public_key_2, modulus)
    print(f"The encryption key is {ans1}.")

    src.copy(ans1)


if __name__ == '__main__':
    main()
