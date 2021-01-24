import src  # My utility functions
import pygame
from pygame.locals import K_UP, K_LEFT, K_DOWN, K_RIGHT, K_p, KEYDOWN, QUIT
import time

INTCODE = src.read(',', ints=True)
INPUTS = {K_UP: 1,
          K_DOWN: 2,
          K_LEFT: 3,
          K_RIGHT: 4}
INSTRUCTIONS = {1: (0, -1, 2),
                2: (0, 1, 1),
                3: (-1, 0, 4),
                4: (1, 0, 3)}


def move_droid(cpu, scale=10):
    x_res = 50
    y_res = 50
    width, height = scale * x_res, scale * y_res
    window = pygame.display.set_mode((width, height))
    tile = pygame.Surface((scale, scale))

    x, y = 25, 25
    dx = dy = 0
    tile.fill((127, 127, 255))
    window.blit(tile, (scale * (x + dx), scale * (y + dy)))
    back = None
    open_squares = {(x, y): (0, back)}
    discovered = set()
    manual = True
    oxygen = None
    while cpu.running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
            if event.type == KEYDOWN:
                if event.key in INPUTS and manual:
                    inp = INPUTS[event.key]
                    dx, dy, back = INSTRUCTIONS[inp]
                    cpu.input.append(inp)
                elif event.key == K_p:
                    manual = not manual

        if not manual:
            for inp, (dx, dy, back) in INSTRUCTIONS.items():
                if (x + dx, y + dy) not in discovered:
                    cpu.input.append(inp)
                    break
            else:
                inp = open_squares[(x, y)][1]
                if inp:
                    dx, dy, back = INSTRUCTIONS[inp]
                    cpu.input.append(inp)
                else:
                    break

        if cpu.input:
            output = cpu.execute()[0]
            if output == 0:
                tile.fill((255, 255, 255))
                window.blit(tile, (scale * (x + dx), scale * (y + dy)))
                discovered.add((x + dx, y + dy))
            else:
                tile.fill((0, 255, 0) if (x, y) == oxygen else (63, 63, 63))
                window.blit(tile, (scale * x, scale * y))
                if (x + dx, y + dy) not in open_squares:
                    open_squares[(x + dx, y + dy)] = open_squares[(x, y)][0] + 1, back
                    discovered.add((x + dx, y + dy))
                x += dx
                y += dy
                tile.fill((63, 63, 191))
                window.blit(tile, (scale * x, scale * y))
                if output == 2:
                    oxygen = (x, y)
        pygame.display.flip()

    front = {oxygen}
    filled = set()
    minutes = -1  # Filling the starting square is minute 0
    while front:
        minutes += 1
        new_front = set()
        for x, y in front:
            filled.add((x, y))
            tile.fill((127, 127, 255))
            window.blit(tile, (scale * x, scale * y))
            for neigh in {(x, y-1), (x, y+1), (x-1, y), (x+1, y)} & open_squares.keys() - filled:
                new_front.add(neigh)
        pygame.display.flip()
        front = new_front
        time.sleep(0.005)
    return open_squares[oxygen][0], minutes


def main(intcode=INTCODE):
    pygame.init()
    cpu = src.IntcodeCPU(intcode)
    ans1, ans2 = move_droid(cpu)
    print("Part One:")
    print(f"The fewest movement commands required to reach the oxygen is {ans1}.")  # 354

    print("\nPart Two:")
    print(f"It takes {ans2} minutes for the area to become oxygenated.")  # 370
    pygame.display.quit()
    src.clip(ans2)


if __name__ == '__main__':
    main()
