import src
from collections import defaultdict, Counter
import re

STRINGS = sorted(src.read())


def sleepiest(strings):
    guards = defaultdict(Counter)
    current_guard = 0
    sleep_minute = 0
    for s in strings:
        if 'Guard' in s:
            current_guard = int(re.search(r'#(\d+) ', s)[1])
        elif 'asleep' in s:
            sleep_minute = int(re.search(r':(\d\d)]', s)[1])
        else:  # Guard wakes up
            wake_minute = int(re.search(r':(\d\d)]', s)[1])
            guards[current_guard] += Counter(range(sleep_minute, wake_minute))
    sleepiest_guard = max(guards.items(), key=lambda i: sum(i[1].values()))
    sleepy_checksum = sleepiest_guard[0] * sleepiest_guard[1].most_common()[0][0]
    consistent_guard = max(guards.items(), key=lambda i: i[1].most_common()[0][1])
    consistent_checksum = consistent_guard[0] * consistent_guard[1].most_common()[0][0]
    return sleepy_checksum, consistent_checksum


def main(strings=None):
    strings = strings or STRINGS

    ans1, ans2 = sleepiest(strings)
    print("Part One:")
    print(f"The result of the multiplication is {ans1}.")  # 4716

    print("\nPart Two:")
    print(f"For the other method, it is {ans2}.")  # 117061
    src.clip(ans2)


if __name__ == '__main__':
    main()
