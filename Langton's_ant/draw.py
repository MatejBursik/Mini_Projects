import pygame, movingAnt

size = int(input("size of spiral (only odd size): "));  FPS = 30;  SIZE = 5;   grid = []
WHITE = (255, 255, 255)    #0
BLACK = (0, 0, 0)    #1

for y in range(size):
    filler=[]
    for x in range(size):
        filler.append("0")
    grid.append(filler)

SCREEN_WIDTH = len(grid)*SIZE;  SCREEN_HEIGHT = len(grid)*SIZE;  ant_Pos = [len(grid)//2, len(grid)//2, "left"]

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
Ant_img = pygame.image.load("Projects\Langton's_ant\Ant_img2.png")
Ant_img = pygame.transform.rotate(Ant_img,45);   Ant_img = pygame.transform.scale(Ant_img,(SIZE,SIZE))

clock = pygame.time.Clock()
counter = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#------code

    clock.tick(FPS)
    square = pygame.Surface([16*SIZE, 16*SIZE])

    previousOrientation = ant_Pos[2]
    returning = movingAnt.move(ant_Pos,grid)
    ant_Pos = returning[0]
    grid = returning[1]


    #turning ant image
    turn = movingAnt.CalcOrientation(previousOrientation,ant_Pos[2])
    Ant_img = pygame.transform.rotate(Ant_img,turn)

    
    #draw grid
    for y,yy in enumerate(grid):
        for x,xx in enumerate(yy):
            if xx == "0":
                square.fill(WHITE)
                screen.blit(square, [x*SIZE, y*SIZE])
            elif xx == "1":
                square.fill(BLACK)
                screen.blit(square, [x*SIZE, y*SIZE])


    #draw ant
    screen.blit(Ant_img, (ant_Pos[0]*SIZE, ant_Pos[1]*SIZE))

    #draw counter
    counter +=1
    myfont = pygame.font.SysFont("Times New Roman", 15)
    text = myfont.render("Moves done: " + str(counter), False, (0, 0, 0))

    screen.blit(text,(0,0))

    pygame.display.update()

#-------
pygame.quit()