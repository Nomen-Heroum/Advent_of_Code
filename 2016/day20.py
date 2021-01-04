import src

BLACKLIST = sorted([tuple(int(n) for n in s.split('-')) for s in src.read(20)])


def lowest_valid(blacklist):
    result = 0
    for lower, upper in blacklist:
        if lower <= result <= upper:
            result = upper + 1
        elif lower > result:
            break
    return result


def count_allowed(blacklist, space=1 << 32):
    allowed = space
    old_up = -1
    for lower, upper in blacklist:
        if upper > old_up:
            allowed -= upper - max(old_up + 1, lower) + 1
            old_up = upper
    return allowed


def main(blacklist=None):
    blacklist = blacklist or BLACKLIST

    print("Part One:")
    ans1 = lowest_valid(blacklist)
    print(f"The lowest valid IP is {ans1}.")

    print("\nPart Two:")
    ans2 = count_allowed(blacklist)
    print(f"{ans2} IPs are allowed by the blacklist.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
