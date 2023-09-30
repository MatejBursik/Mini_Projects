import numpy as np
import pygame

class Curve:
    def __init__(self, points):
        self.points = np.array(points)

    # copy, transform, and add to the existing array of cordinates
    def rotate(self,window,scale):
        new = np.copy(self.points)
        pivot = np.copy(self.points[self.points.shape[0]-1])

        # transformation 
        new -= pivot
        new = np.flip(new, 1)
        new *= [-1,1]
        new += pivot
        new = np.flip(new, 0)
        self.points = np.insert(self.points, self.points.shape[0], new[1:], axis=0) # insert new points except pivot
        pygame.draw.aalines(window, (0,0,0), False, self.points[self.points.shape[0]//2:]*scale) # draw the new half

    # re-centralize based on first_end
    def scale_update(self,window,scale):
        center = [(pygame.display.Info().current_w/scale)/2, (pygame.display.Info().current_h/scale)/2]
        diff = center - self.points[0]
        self.points += diff
        pygame.draw.rect(screen,(255,255,255), pygame.Rect(0,0,pygame.display.Info().current_w, pygame.display.Info().current_h))
        pygame.draw.aalines(window, (0,0,0), False, self.points*scale)
        print(scale)

pygame.init()
screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h), pygame.NOFRAME)
clock = pygame.time.Clock()

running = True
scale = 20

# starting points
first_end = [(pygame.display.Info().current_w/scale)/2, (pygame.display.Info().current_h/scale)/2]
first_pivot = [first_end[0], first_end[1]+1]
curve = Curve(np.array([first_end,first_pivot]))

# initial draw
pygame.draw.rect(screen,(255,255,255), pygame.Rect(0,0,pygame.display.Info().current_w,pygame.display.Info().current_h))
pygame.draw.aalines(screen, (0,0,0), False, curve.points*scale)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            # window scaling
            if event.key == pygame.K_z: # down
                scale *= 0.9
                curve.scale_update(screen,scale)
            if event.key == pygame.K_x: # up
                scale *= 1.1
                curve.scale_update(screen,scale)

            # rotate
            if event.key == pygame.K_c:
                curve.rotate(screen,scale)
    
    pygame.display.update()
    clock.tick(60)
