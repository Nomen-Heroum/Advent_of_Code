import src
import regex as re

STREAM = src.read()[0]


def find_score(stream):
    stream = re.sub(r'!.', '', stream)
    garbage_chars = sum(len(s) for s in re.findall(r'<(.*?)>', stream))  # Part 2
    stream = re.sub(r'<.*?>', '', stream)  # Clean the stream
    groups = [stream.replace(',', '')[1:-1]]
    level = 1
    score = 0
    while groups:
        score += level * len(groups)
        new = []
        for g in groups:
            new += re.findall('{((?R)*)}', g)
        level += 1
        groups = new
    return score, garbage_chars


def main(stream=STREAM):
    ans1, ans2 = find_score(stream)
    print("Part One:")
    print(f"The total score for all groups is {ans1}.")  # 11898

    print("\nPart Two:")
    print(f"There are {ans2} non-canceled characters within the garbage.")  # 5601
    src.copy(ans2)


if __name__ == '__main__':
    main()
