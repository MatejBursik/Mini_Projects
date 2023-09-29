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
    def scale_update(self,window,zoom,scale):
        scaled_window = pygame.transform.scale_by(pygame.Surface.copy(window), zoom)
        pygame.draw.rect(window,(255,255,255), pygame.Rect(0,0,pygame.display.Info().current_w, pygame.display.Info().current_h))
        window.blit(scaled_window, (((pygame.display.Info().current_w / (scale*2)) - scaled_window.get_width()/2), ((pygame.display.Info().current_h / (scale*2)) - scaled_window.get_height()/2)))
        print(scale) # !!! no idea why the positioning of the scaled_window is wrong; also why everything disapears when zooming in

"""
processing issue (solution):
- add a window which scales and is pasted back onto the game window
- zoom affects the window not the curve(line based on points)
"""

pygame.init()
screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h), pygame.NOFRAME)
clock = pygame.time.Clock()

running = True
scale = 20

# starting points
first_end = [pygame.display.Info().current_w / (scale*2), pygame.display.Info().current_h / (scale*2)]
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
                zoom = 0.9
                scale *= zoom
                curve.scale_update(screen,zoom,scale)
            if event.key == pygame.K_x: # up
                zoom = 1.1
                scale *= zoom
                curve.scale_update(screen,zoom,scale)

            # rotate
            if event.key == pygame.K_c:
                curve.rotate(screen,scale)
    
    pygame.display.update()
    clock.tick(60)
