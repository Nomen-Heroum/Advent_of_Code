import src
import re

STRINGS = src.read()


def evaluate(string: str):
    """Evaluate a simple string of numbers and operators without parentheses"""
    numbers = [int(s) for s in re.findall(r'\d+', string)]
    operators = re.findall(r'[*+]', string)
    assert len(numbers) == len(operators) + 1, "Unexpected amount of numbers/operators."
    outcome = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            outcome += numbers[i + 1]
        if op == '*':
            outcome *= numbers[i + 1]
    return outcome


def evaluate_2(string: str):
    while '+' in string:
        string = re.sub(r'\d+ \+ \d+', lambda mo: str(evaluate(mo[0])), string)
    return evaluate(string)


def calculate(string: str, ev: callable):
    while '(' in string:
        string = re.sub(r'\(([^()]+)\)', lambda mo: str(ev(mo[1])), string)
    return ev(string)


def total_sum(strings: list, ev=evaluate):
    return sum(calculate(s, ev) for s in strings)


def main(strings=STRINGS):
    print("Part One:")
    ans1 = total_sum(strings)
    print(f"The sum of outcomes is {ans1}.")

    print("\nPart Two:")
    ans2 = total_sum(strings, evaluate_2)
    print(f"The sum of outcomes is now {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
