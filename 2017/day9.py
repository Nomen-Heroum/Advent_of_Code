import src
import re

STREAM = src.read()[0]


def find_score(stream):
    stream = re.sub(r'!.', '', stream)  # Remove escaped characters
    garbage_chars = sum(len(s) for s in re.findall(r'<(.*?)>', stream))  # Count the garbage
    stream = re.sub(r',|<.*?>', '', stream)  # Clean the stream
    level = 0
    score = 0
    for char in stream:
        if char == '{':
            level += 1
            score += level
        else:
            level -= 1
    return score, garbage_chars


def main(stream=STREAM):
    ans1, ans2 = find_score(stream)
    print("Part One:")
    print(f"The total score for all groups is {ans1}.")  # 11898

    print("\nPart Two:")
    print(f"There are {ans2} non-canceled characters within the garbage.")  # 5601
    src.clip(ans2)


if __name__ == '__main__':
    main()
