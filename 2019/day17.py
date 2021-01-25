import src  # My utility functions
import re

INTCODE = src.read(',', ints=True)


def alignment(cpu):
    output = cpu.execute()
    view = ''.join(chr(n) for n in output).strip()
    print(view)

    scaffolding = set()
    view = view.splitlines()
    bot = None
    heading = {'^': -1j, 'v': 1j, '<': -1, '>': 1}
    for y, line in enumerate(view):
        for x, char in enumerate(line):
            if char == '#':
                scaffolding.add(x + y*1j)
            elif char in heading:
                position = x + y*1j
                scaffolding.add(position)
                bot = position, heading[char]

    total = 0
    for z in scaffolding:
        if {z-1, z+1, z-1j, z+1j}.issubset(scaffolding):
            total += z.real * z.imag
    return int(total), scaffolding, bot


def plan_movement(scaffolding, bot, cpu):
    # First build the most straightforward path
    position, direction = bot
    path = ''
    forward = 0
    while True:
        if position + direction in scaffolding:
            position += direction
            forward += 1
        else:
            if forward:
                path += str(forward) + ','
                forward = 0
            if position + 1j * direction in scaffolding:
                direction *= 1j
                path += 'R,'
            elif position - 1j * direction in scaffolding:
                direction *= -1j
                path += 'L,'
            elif path:
                break
            else:
                direction *= -1
                path += 'R,R,'

    # Regex inspired by /u/Sephibro
    mo = re.fullmatch(r'(.{1,21})\1*(.{1,21})(?:\1|\2)*(.{1,21})(\1|\2|\3)*', path)
    funcs = [mo[i+1].strip(',') for i in range(3)]
    routine = path.strip(',').replace(funcs[0], 'A').replace(funcs[1], 'B').replace(funcs[2], 'C')
    return '\n'.join([routine] + funcs) + '\nn\n'


def main(intcode=INTCODE):
    cpu = src.IntcodeCPU(intcode)
    cpu.memory[0] = 2
    ans1, scaffolding, bot = alignment(cpu)  # 3336
    print("Part One:")
    print(f"The sum of alignment parameters is {ans1}.")

    print("\nPart Two:")
    instructions = plan_movement(scaffolding, bot, cpu)
    cpu.input += [ord(c) for c in instructions]
    output = cpu.execute()
    ans2 = output[-1]  # 597517
    print(f"The vacuum bot collects {ans2} dust.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
