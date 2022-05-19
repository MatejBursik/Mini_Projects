import structure

spiral = structure.spiral
print(spiral)

import pygame
pygame.init()
WHITE = (255, 255, 255);    BLACK = (0, 0, 0);  SIZE = 1;  SCREEN_WIDTH = len(spiral)*SIZE;  SCREEN_HEIGHT = len(spiral)*SIZE

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    square = pygame.Surface([SIZE, SIZE])
    square.fill(BLACK)

    for y,yy in enumerate(spiral):
        for x,xx in enumerate(yy):
            if xx == "X":
                screen.blit(square, [x*SIZE, y*SIZE])
    pygame.display.update()

pygame.quit()