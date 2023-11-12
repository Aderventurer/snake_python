import pygame


def drawGrid(width, rows, surface):
    sizeBetween = width // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBetween
        y = y + sizeBetween

        pygame.draw.line(surface, (0, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surface, (0, 255, 255), (0, y), (width, y))


def main():
    pygame.init()
    pygame.display.set_caption("贪吃蛇")
    width = 500
    hight = 500
    size = (width, hight)
    rows = 20
    window = pygame.display.set_mode(size)

    quit = False
    while not quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Game Finished")
                quit = True
        drawGrid(width, rows, window)
        pygame.display.flip()


if __name__ == "__main__":
    main()
