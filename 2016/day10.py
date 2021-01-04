import src
from collections import defaultdict
from parse import parse

INSTRUCTIONS = sorted(src.read(10))


def run(instructions):
    gives = {}
    bots = defaultdict(set)
    outputs = defaultdict(list)
    the_bot = []
    the_output = []

    def give(n, v, t='bot'):
        if t == 'bot':
            bots[n].add(v)
            if len(bots[n]) == 2:
                if bots[n] == {17, 61}:
                    the_bot.append(n)
                out = gives[n]
                low_high = sorted(list(bots[n]))
                for i, (typ, num) in enumerate(out):
                    give(num, low_high[i], typ)
        else:
            outputs[n].append(v)
            if outputs[0] and outputs[1] and outputs[2]:
                the_output.append(outputs[0][0] * outputs[1][0] * outputs[2][0])

    for instr in instructions:
        if 'gives' in instr:
            bot, type1, num1, type2, num2 = parse('bot {:d} gives low to {} {:d} and high to {} {:d}', instr)
            gives[bot] = ((type1, num1), (type2, num2))
        else:
            value, bot = parse('value {:d} goes to bot {:d}', instr)
            give(bot, value)
    return the_bot[0], the_output[0]


def main(instructions=None):
    instructions = instructions or INSTRUCTIONS

    print("Part One:")
    ans1, ans2 = run(instructions)
    print(f"The bot that compares 61 and 17 is {ans1}.")

    print("\nPart Two:")
    print(f"The product of chip values in outputs 0-2 is {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
