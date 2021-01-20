import src

PASSWORD_RANGE = range(264793, 803935 + 1)


def count_valid(password_range):
    count_1 = 0
    count_2 = 0
    for number in password_range:
        double = False  # "Double digit" criterion
        group_size = 1  # Number of similar digits strung together
        isolated_double = False  # Part 2 criterion
        increasing = True  # "No decreases" criterion
        digit = 10
        while number:
            number, new_digit = divmod(number, 10)  # Checking from right to left
            if new_digit > digit:
                increasing = False
                break
            elif new_digit == digit:
                group_size += 1
                double = True
            else:
                if group_size == 2:
                    isolated_double = True
                group_size = 1
            digit = new_digit
        if increasing and double:
            count_1 += 1
            if isolated_double or group_size == 2:
                count_2 += 1
    return count_1, count_2


def main(password_range=PASSWORD_RANGE):
    ans1, ans2 = count_valid(password_range)
    print("Part One:")
    print(f"There are {ans1} valid passwords in the given range.")  # 966

    print("\nPart Two:")
    print(f"With the stricter criteria, {ans2} passwords are valid.")  # 628
    src.clip(ans2)


if __name__ == '__main__':
    main()
