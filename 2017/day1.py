import src

STRING = src.read()[0]


def solve_captcha(string, version=1):
    n = len(string)
    step = 1 if version == 1 else n//2
    return sum(int(char) for i, char in enumerate(string) if string[(i+step) % n] == char)


def main(string=STRING):
    print("Part One:")
    ans1 = solve_captcha(string)  # 1158
    print(f"The solution to my captcha is {ans1}.")

    print("\nPart Two:")
    ans2 = solve_captcha(string, version=2)  # 1132
    print(f"The solution to the second captcha is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
