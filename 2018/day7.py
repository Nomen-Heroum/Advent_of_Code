import src
import re
from collections import defaultdict
from copy import deepcopy

STRING = src.read('\n\n')[0]


def follow_instruction(current_step, requirements):
    del requirements[current_step]
    for step in requirements:
        requirements[step] -= {current_step}


def assemble_sleigh(requirements):
    order = ''
    while requirements:
        current_step = min(requirements.items(), key=lambda i: (len(i[1]), i[0]))[0]
        order += current_step
        follow_instruction(current_step, requirements)
    return order


def assemble_sleigh_together(requirements, workers=5):
    current_time = 0
    assigned = {}
    while requirements:
        available = sorted(step for step in requirements  # All unstarted tasks with 0 requirements
                           if len(requirements[step]) == 0
                           and step not in assigned)
        for step in available:
            assigned[step] = ord(step) - 4  # ord('A') is 65
            if len(assigned) == workers:  # Maximum amount of assigned tasks is workers
                break

        shortest_wait = min(assigned.values())
        current_time += shortest_wait
        for step in deepcopy(assigned):  # Copy to prevent dict mutation during the loop
            if assigned[step] == shortest_wait:  # Task is finished
                del assigned[step]
                follow_instruction(step, requirements)
            else:
                assigned[step] -= shortest_wait
    return current_time


def main(string=STRING):
    pattern = re.compile(r"Step (\w) must be finished before step (\w) can begin\.")
    requirements = defaultdict(set)
    for required, step in pattern.findall(string):
        requirements[required] |= set()  # Assures every step is in the dictionary
        requirements[step].add(required)

    print("Part One:")
    ans1 = assemble_sleigh(deepcopy(requirements))  # OKBNLPHCSVWAIRDGUZEFMXYTJQ
    print(f"The assembly order is {ans1}.")

    print("\nPart Two:")
    ans2 = assemble_sleigh_together(deepcopy(requirements))  # 982
    print(f"With 5 workers, it takes {ans2} seconds to finish the sleigh.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
