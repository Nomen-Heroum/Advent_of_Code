import src

NUMBERS = [19, 20, 14, 0, 9, 1]


def play(numbers, end):
    while len(numbers) < end:
        try:
            numbers.append(numbers[:-1][::-1].index(numbers[-1]) + 1)
        except ValueError:
            numbers.append(0)
    return numbers[-1]


def play2(numbers, end):
    dictionary = {k: i+1 for i, k in enumerate(numbers[:-1])}
    last = numbers[-1]
    for i in range(len(numbers), end):
        if last in dictionary:
            newlast = i - dictionary[last]
        else:
            newlast = 0
        dictionary[last] = i
        last = newlast
    return last


def main(numbers=None):
    numbers = numbers or NUMBERS

    src.one()
    ans1 = play(numbers, 2020)
    print(f"The 2020th number spoken is {ans1}.")
    
    src.two()
    ans2 = play2(numbers, 30000000)
    print(f"The 30000000th number spoken is {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
