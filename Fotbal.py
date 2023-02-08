import pygame
import random
import sys
roz_X = 1500
roz_Y = 900
boost = 0
pygame.init()
okno = pygame.display.set_mode((roz_X, roz_Y))
hodiny = pygame.time.Clock()
FPS = 120
def gradientRect( window, left_colour, right_colour, target_rect ):
    colour_rect = pygame.Surface( ( 2, 2 ) )
    pygame.draw.line( colour_rect, left_colour, ( 0,0 ), ( 0,1 ) )
    pygame.draw.line( colour_rect, right_colour, ( 1,0 ), ( 1,1 ) )
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )
    window.blit( colour_rect, target_rect )
while True:
    hodiny.tick(FPS)
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RSHIFT] and boost > 0.3:
        rychlost = 2
        boost -= 0.3
    if keys[pygame.K_RSHIFT] == False or boost < 0.4 :
        rychlost = 1
        boost += 0.1
    if boost > 136:
        boost = 136
    okno.fill((192,192,192))
    pygame.draw.rect(okno, (0,0,0), (roz_X - 280, roz_Y - 100, 140, 50),2)
    gradientRect( okno, (255, 255, 0), (255, 0, 0), pygame.Rect( roz_X - 278,roz_Y - 98, boost, 46 ) )
    pygame.display.update()