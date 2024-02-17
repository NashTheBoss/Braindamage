import pygame

DISPLAY_WIDTH =  1280
DISPLAY_HEIGHT = 720

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

while True:
    pygame.event.get
    if pygame.event == quit:
        pygame.quit
    pygame.draw.circle(screen, (255,0,0), center = (DISPLAY_WIDTH/2 ,DISPLAY_HEIGHT/2), radius = 20)
    pygame.display.update()