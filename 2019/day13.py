import src  # My utility functions
import pygame
from pygame.locals import K_LEFT, K_DOWN, K_RIGHT, K_p, KEYDOWN, QUIT

INTCODE = src.read(',', ints=True)
COLOURS = {0: (0, 0, 0),
           1: (255, 0, 0),
           2: (0, 255, 0),
           3: (0, 0, 255),
           4: (255, 255, 255)}
INPUTS = {K_LEFT: -1,
          K_DOWN: 0,
          K_RIGHT: 1}


def play_game(cpu, scale=15):
    cpu.memory[0] = 2

    x_res = 45
    y_res = 23
    width, height = scale * x_res, scale * y_res
    window = pygame.display.set_mode((width, height))
    tile = pygame.Surface((scale, scale))

    block_count = 0
    score = 0
    manual = True
    ball_x = 0
    paddle_x = 0
    while cpu.running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
            if event.type == KEYDOWN:
                if event.key in INPUTS and manual:
                    cpu.input.append(INPUTS[event.key])
                elif event.key == K_p:
                    manual = not manual

        if not manual:
            if paddle_x < ball_x:
                cpu.input.append(1)
            elif paddle_x > ball_x:
                cpu.input.append(-1)
            else:
                cpu.input.append(0)

        output = cpu.execute()
        instructions = [output[n:n+3] for n in range(0, len(output), 3)]
        for x, y, out in instructions:
            if (x, y) == (-1, 0):
                score = out
                print(f"Score = {score}. Press P to start/pause autopilot.\r", end='')
            else:
                tile.fill(COLOURS[out])
                window.blit(tile, (scale * x, scale * y))
                if out == 4:
                    ball_x = x
                elif out == 3:
                    paddle_x = x
                elif out == 2:
                    block_count += 1
        pygame.display.flip()
    pygame.display.quit()
    return block_count, score


def main(intcode=INTCODE):
    pygame.init()
    cpu = src.IntcodeCPU(intcode)
    ans1, ans2 = play_game(cpu)
    print("Part One:")
    print(f"{ans1} block tiles are on screen when the game starts.")  # 357

    print("\nPart Two:")
    print(f"After breaking all blocks, my score is {ans2}.")  # 17468
    src.clip(ans2)


if __name__ == '__main__':
    main()
