from game import *
import pygame

pygame.init()

size = width, height = 1000, 1000

square_size = 10


glife = GameOfLife(width//square_size, height//square_size)
glife.randomize_grid()

screen = pygame.display.set_mode(size)
light_blue = pygame.Color(173, 216, 230)

done = False
while not done:
    screen.fill(pygame.Color(0,0,0))

    # draw
    for row in range(glife.width):
        for col in range(glife.height):
            if glife.grid[row][col]:
                ex = pygame.Rect(
                        row*square_size, col*square_size,
                        square_size, square_size)
                pygame.draw.rect(screen, light_blue, ex)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.update()

    glife.update_grid()
