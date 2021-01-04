import src

POSITION = (3010, 3019)


def get_code(position):
    row, column = position
    code_number = (row + column - 2)*(row + column - 1)//2 + column
    return (20151125 * pow(252533, code_number - 1, 33554393)) % 33554393


def main(position=POSITION):
    print("Part One:")
    ans1 = get_code(position)
    print(f"The code is {ans1}.")

    src.copy(ans1)


if __name__ == '__main__':
    main()
