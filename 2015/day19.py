import src
import re
from collections import defaultdict

INSTR, MOLECULE = src.read(19, '\n\n')
MATCH = re.finditer(r'(\w+) => (\w+)', INSTR)
DICT = defaultdict(list)
TUPLIST = []
for MO in MATCH:
    DICT[MO[1]].append(MO[2])
    TUPLIST.append((MO[2], MO[1]))
ORDER = sorted(TUPLIST[:-3], key=lambda x: -len(x[0]))


def count_mutations(dct, molecule):
    mutations = defaultdict(int)
    for key in dct:
        match = re.finditer(key, molecule)
        for mo in match:
            for repl in dct[key]:
                new = molecule[:mo.start()] + repl + molecule[mo.end():]
                mutations[new] += 1
    return len(mutations)


def depth_first_medicine(order, molecule, i=2):
    for o in order:
        if o[0] in molecule:
            new = molecule.replace(o[0], o[1], 1)
            if new in ['HF', 'NAl', 'OMg']:
                return i
            return depth_first_medicine(order, new, i+1)


def main(dct=None, order=None, molecule=MOLECULE):
    dct = dct or DICT
    order = order or ORDER

    src.one()
    distinct = count_mutations(dct, molecule)
    print(f"There are {distinct} distinct molecules to be made with one replacement.")

    src.two()
    medicine = depth_first_medicine(order, molecule)
    print(f"It takes at least {medicine} alterations to make the medicine.")
    src.copy(medicine)


if __name__ == '__main__':
    main()


# def make_medicine(dct, target_molecule):
#     current = {'e'}
#     for i in itertools.count(1):
#         newset = set()
#         for molecule in current:
#             for key in dct:
#                 match = re.finditer(key, molecule)
#                 for mo in match:
#                     for repl in dct[key]:
#                         new = molecule[:mo.start()] + repl + molecule[mo.end():]
#                         if new == target_molecule:
#                             return i
#                         newset.add(new)
#         current = newset


# def make_medicine(dct, target_molecule):
#     current = {target_molecule}
#     for i in itertools.count(1):
#         newset = set()
#         for molecule in current:
#             for key, vals in dct.items():
#                 for val in vals:
#                     match = re.finditer(val, molecule)
#                     for mo in match:
#                         new = molecule[:mo.start()] + key + molecule[mo.end():]
#                         if new == 'e':
#                             return i
#                         newset.add(new)
#         current = newset
