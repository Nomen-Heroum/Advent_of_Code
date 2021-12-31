import src  # My utility functions
from statistics import median

STRINGS = src.read()
PAIRS = {'(': ')',
         '[': ']',
         '{': '}',
         '<': '>'}

SCORES = {')': 3,
          ']': 57,
          '}': 1197,
          '>': 25137}

VALUES = {')': 1,
          ']': 2,
          '}': 3,
          '>': 4}


def score(strings):
    error_score = 0
    completion_scores = []
    for string in strings:
        incomplete = True
        current = []
        for char in string:
            if char in PAIRS:
                current.append(char)
            elif char != PAIRS[current.pop(-1)]:
                error_score += SCORES[char]
                incomplete = False
                break

        if incomplete:
            complete_score = 0
            for char in current[::-1]:
                complete_score *= 5
                complete_score += VALUES[PAIRS[char]]
            completion_scores.append(complete_score)

    return error_score, median(completion_scores)


def main(strings=STRINGS):
    ans1, ans2 = score(strings)  # 399153, 2995077699
    print("Part One:")
    print(f"The total syntax error score for corrupted lines is {ans1}.")

    print("\nPart Two:")
    print(f"The winning completion score is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
