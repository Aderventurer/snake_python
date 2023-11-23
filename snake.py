import pygame
import random


class Point:
    row = 0
    col = 0

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def copy(self):
        return Point(row=self.row, col=self.col)


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
    snake_color = (200, 200, 230)

    head = Point(row=10, col=10)
    head_color = (255, 0, 0)
    snakes = [
        Point(row=head.row, col=head.col+1),
        Point(row=head. row, col=head.col+2),
        Point(row=head. row, col=head.col+3)
    ]

    def gen_food():
        while 1:
            pos = Point(row=random.randint(0, rows-1),
                        col=random.randint(0, cols-1))
            is_coll = False
            if head.row == pos. row and head.col == pos.col:
                is_coll = True
            for snake in snakes:
                if snake.row == pos.row and snake.col == pos.col:
                    is_coll = True
                    break
                if not is_coll:
                    break
        return pos

    food = gen_food()
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

    rect(head, head_color)
    rect(food, food_color)

    quit = False

    clock = pygame.time.Clock()
    direct = 'left'
    while not quit:
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Game Finished")
                quit = True
            elif event. type == pygame.KEYDOWN:
                if event.key == 273 or event.key == 100:
                    direct = 'up'
                elif event.key == 274 or event.key == 115:
                    direct = 'down'
                elif event.key == 276 or event.key == 97:
                    direct = 'left'
                elif event.key == 275 or event.key == 119:
                    direct = 'right'

        # 吃东西
        eat = (head.row == food.row and head.col == food.col)
        # 重新产生食物
        if eat:
            food = gen_food()

        # 处理身子
        # 1.吧原来的头，插入到snakes的头上
        snakes.insert(0, head.copy())
        # 2.把snakes的最后一个删掉
        if not eat:
            snakes.pop()

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
        rect(head, head_color)
        rect(food, food_color)
        for snake in snakes:
            rect(snake, snake_color)
        pygame.display.flip()
        clock.tick(10)


if __name__ == "__main__":
    main()
