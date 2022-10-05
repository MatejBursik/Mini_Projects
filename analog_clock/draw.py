import pygame, getTime, math

size = 1000;  FPS = 30;  WHITE = (255, 255, 255);  BLACK = (0, 0, 0);   RED = (255, 0, 0);   BLUE = (0, 0, 255);    SCREEN_WIDTH = size;  SCREEN_HEIGHT = size


pygame.init()
pygame.font.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
img_Clock = pygame.image.load("analog_clock\\img_clock.png")
img_Clock = pygame.transform.scale(img_Clock, (250, 250))
clock = pygame.time.Clock()

#variables
Diff = 360/60



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#------code
    clock.tick(FPS)
    screen.fill(WHITE)
    screen.blit(img_Clock, (151, 100))
    screen.blit(img_Clock, (151, 700))

    #gmt_0
    gmt_0 = getTime.get_GMT_0()

    #smh[ sec, min, hour]
    smh = [math.radians(Diff*int(gmt_0[17:19])-90), math.radians(Diff*int(gmt_0[14:16])-90), math.radians(Diff*int(gmt_0[11:13])-90)]
    smh.reverse()

    for i,unit in enumerate(smh):
        MovingPoint_Y = 125*math.sin(unit)
        MovingPoint_X = 125*math.cos(unit)
        if i == 0:
            Color = BLACK
            Thick = 9
        elif i == 1:
            Color = BLUE
            Thick = 6
        else:
            Color = RED
            Thick = 3
        pygame.draw.line(screen, Color, (275, 225), (275 + MovingPoint_X, 225 + MovingPoint_Y), Thick)
    

    
    
    #gmt_local
    gmt_local = getTime.get_GMT_local()

    #smh[ sec, min, hour]
    smh = [math.radians(Diff*int(gmt_local[17:19])-90), math.radians(Diff*int(gmt_local[14:16])-90), math.radians(Diff*int(gmt_local[11:13])-90)]
    smh.reverse()

    for i,unit in enumerate(smh):
        MovingPoint_Y = 125*math.sin(unit)
        MovingPoint_X = 125*math.cos(unit)
        if i == 0:
            Color = BLACK
            Thick = 9
        elif i == 1:
            Color = BLUE
            Thick = 6
        else:
            Color = RED
            Thick = 3
        pygame.draw.line(screen, Color, (275, 825), (275 + MovingPoint_X, 825 + MovingPoint_Y), Thick)


     
    
    #text drawing

    myfont = pygame.font.SysFont("Serif", 25)
    drw_gmt_0 = myfont.render("←  GMT 0: "+ gmt_0, False, BLACK)
    drw_gmt_local = myfont.render("←  Local time: " + gmt_local, False, BLACK)
    colorInfo = myfont.render("Black represents hours, Blues represents minutes, Red represents seconds", False, BLACK)

    
    screen.blit(drw_gmt_0,(SCREEN_WIDTH/2,SCREEN_HEIGHT/5))
    screen.blit(drw_gmt_local,(SCREEN_WIDTH/2,SCREEN_HEIGHT-(SCREEN_HEIGHT/5)))
    screen.blit(colorInfo,(0,0))

   

    pygame.display.update()

#-------
pygame.quit()