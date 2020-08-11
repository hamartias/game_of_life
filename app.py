from game import *
import pygame

pygame.init()

size = width, height = 1000, 1000


glife = GameOfLife(width//10, height//10)
glife.randomize_grid()

screen = pygame.display.set_mode(size)
grey = pygame.Color(211, 211, 211)

done = False
while not done:
    screen.fill(pygame.Color(0,0,0))

    # draw
    for row in range(glife.width):
        for col in range(glife.height):
            if glife.grid[row][col]:
                ex = pygame.Rect(row*10, col*10, 10, 10)
                pygame.draw.rect(screen, grey, ex)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.update()

    glife.update_grid()
