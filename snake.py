import pygame
pygame.init()
width = 500
hight = 500
size = (width,hight)
rows = 20
pygame. display.set_mode (size)
window = pygame . display.set_mode (size)
pygame .display .set_caption("贪吃蛇")
quit = True 
clock=pygame.time.Clock ()
clock.tick (60)
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y +sizeBtwn

        pygame.draw.line(surface, (0,255,255), (x, 0),(x,w))
        pygame.draw.line(surface, (0,255,255), (0, y),(w,y))
while quit:
    for event in pygame.event.get () :
        
        if event. type==pygame. QUIT:
            
            quit = False
    drawGrid(width,rows,window)          
    pygame.display.flip()