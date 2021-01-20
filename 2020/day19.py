import src
import regex

STRINGS = src.read(split='\n\n')
RULES = STRINGS[0].split('\n')
MESSAGES = STRINGS[1].split('\n')


def rules_dict(rules: list, version=1):
    dct = {}
    for rule in rules:
        key, value = rule.split(': ')
        if '"' in value:
            dct[key] = lambda v=value[1]: v
            continue
        nums = regex.findall(r'\d+', value)
        half = len(nums)//2
        if '|' in value:
            dct[key] = lambda ns=nums, n=half: (f"({''.join(dct[num]() for num in ns[:n])}"
                                                f"|{''.join(dct[num]() for num in ns[n:])})")
        else:
            dct[key] = lambda ns=nums: ''.join(dct[num]() for num in ns)
    if version > 1:
        dct['8'] = lambda: f"({dct['42']()})+"
        dct['11'] = lambda: f"(?P<rule>{dct['42']()}(?&rule)?{dct['31']()})"
    return dct


def count_matches(rules, messages, version=1):
    dct = rules_dict(rules, version)
    return sum(bool(regex.fullmatch(dct['0'](), m)) for m in messages)


def main(rules=RULES, messages=MESSAGES):
    print("Part One:")
    ans1 = count_matches(rules, messages)
    print(f"The number of valid messages is {ans1}.")

    print("\nPart Two:")
    ans2 = count_matches(rules, messages, version=2)
    print(f"There are now {ans2} valid messages.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
