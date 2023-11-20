import pygame
import random


class Point:
    row = 0
    col = 0

    def __init__(self, row, col):
        self.row = row
        self.col = col


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
    highth = 500
    size = (width, highth)
    rows = 20
    cols = 20
    window = pygame.display.set_mode(size)

    head = Point(row=10, col=10)
    head_color = (255, 0, 0)
    direct = 'left'
    food = Point(row=random.randint(0, rows-1), col=random.randint(0, cols-1))
    food_color = (255, 255, 0)

    def rect(point, color):
        cell_width = width/cols
        cell_height = highth/rows
        left = point.col * cell_width
        top = point.row * cell_height

        pygame.draw.rect(
            window, color,
            (left, top, cell_width, cell_height)
        )
        pass

    rect(head, head_color)
    rect(food, food_color)

    quit = False
    clock = pygame.time.Clock()
    while not quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Game Finished")
                quit = True
            elif event. type == pygame.KEYDOWN:
                if event.key == 273 or event.key == 119:
                    direct = 'up'
                elif event.key == 274 or event.key == 115:
                    direct = 'down'
                elif event.key == 276 or event.key == 97:
                    direct = 'left'
                elif event.key == 275 or event.key == 100:
                    direct = 'right'
        # 移动
        if direct == 'left':
            head.col -= 1
        elif direct == 'right':
            head. row -= 1
        elif direct == 'up':
            head.col += 1
        elif direct == 'down':
            head.row += 1

        drawGrid(width, rows, window)
        pygame.display.flip()
        clock.tick(10)


if __name__ == "__main__":
    main()
