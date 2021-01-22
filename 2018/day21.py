import src  # My utility functions

STRINGS = src.read()
SET_VALUE = int(STRINGS[8].split()[1])


def calculate_registers(reg_3=65536, reg_4=SET_VALUE):
    while reg_3:
        reg_3, remainder = divmod(reg_3, 256)
        reg_4 = ((reg_4 + remainder) * 65899) % 16777216  # 2^24
    return reg_3, reg_4


def find_highest():
    seen = set()
    old_reg_4 = 0
    while True:
        reg_3 = old_reg_4 | 65536
        reg_4 = SET_VALUE
        reg_3, reg_4 = calculate_registers(reg_3, reg_4)
        if reg_4 in seen:
            return old_reg_4
        seen.add(reg_4)
        old_reg_4 = reg_4


def main():
    print("Part One:")
    _, ans1 = calculate_registers()  # 15690445
    print(f"The program halts most quickly with {ans1} in register 0.")

    print("\nPart Two:")
    ans2 = find_highest()  # 936387
    print(f"The program takes longest to halt with {ans2} in register 0.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
