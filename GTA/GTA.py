import pygame

DISPLAY_WIDTH =  1280
DISPLAY_HEIGHT = 720

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
x=0
def bewegung():
    global x
    x=x+1
#gemeloope
while True:
    pygame.event.get
    if pygame.event == quit:
        pygame.quit
    pygame.draw.circle(screen, (255,0,0), center = (x ,DISPLAY_HEIGHT/2), radius = 20)
    bewegung()
    pygame.display.update()