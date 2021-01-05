import src
import re

pp_strings = src.read(split='\n\n')


def read_pp(pp_string):
    passport = re.split(r"[\n ]", pp_string)
    return passport


def is_valid(passport, version):
    important_stuff = [stuff for stuff in passport if stuff[:3] != 'cid']
    if len(important_stuff) == 7:
        if version == 1:
            return True
        data = dict(s.split(':') for s in important_stuff)
        conditions = [1920 <= int(data['byr']) <= 2002,
                      2010 <= int(data['iyr']) <= 2020,
                      2020 <= int(data['eyr']) <= 2030,
                      re.fullmatch(r'1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in', data['hgt']),
                      re.fullmatch(r'#[0-9a-f]{6}', data['hcl']),
                      re.fullmatch(r'amb|blu|brn|gry|grn|hzl|oth', data['ecl']),
                      re.fullmatch(r'\d{9}', data['pid'])]
        return all(conditions)
    return False


def count_valid(strings=pp_strings, version=2):
    passports = (read_pp(s) for s in strings)
    count = sum(is_valid(pp, version=version) for pp in passports)
    print(f"{count} passports are valid out of {len(strings)}.")
    return count


src.copy(count_valid(version=1))

print("\nPart Two:")
src.copy(count_valid())
