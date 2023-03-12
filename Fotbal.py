import pygame, sys, random, math, time

pygame.init()
roz_X = 1920 
roz_Y = 1080 
velikost = 100
poz_X = roz_X / 4
poz_Y = roz_Y / 2 - 50

poz_X2 = roz_X / 1.5
poz_Y2 = roz_Y / 2 - 50

vykresleni1 = True
vykresleni2 = True 
hodiny = pygame.time.Clock()
rychlost2 = 1
rychlost1 = 1
boost1 = 100
boost2 = 100
FPS = 120
okno = pygame.display.set_mode((roz_X, roz_Y))
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 60)
counter, text = 120, '120'.rjust(3)
time1 = 99999999999999999999999999999999999999999999999999
time2 = 99999999999999999999999999999999999999999999999999

cubes = []
for i in range(3):
    rect = pygame.Rect(random.randint(25,roz_X - 50), random.randint(25,roz_Y - 50), 30, 30)
    cubes.append(rect)
    
class circle:
    def __init__(self, okno, color, x, y, radius) :
        self.x = x
        self.y = y
        self.radius = radius
        pygame.draw.circle(okno, color, (x, y), radius)
    
    def collidecircle(self, circle):
        if math.sqrt(pow(circle.x-self.x, 2) + pow(circle.y-self.y, 2)) < (self.radius + circle.radius):
            return True
        else :
            return False
        


Ufo_blue = pygame.image.load("Obrazky/UFO-blue.png")
Ufo_blue = pygame.transform.scale(Ufo_blue, (velikost,velikost))
Ufo_red = pygame.image.load("Obrazky/Ufo-red.png")
Ufo_red = pygame.transform.scale(Ufo_red, (velikost,velikost))



def gradientRect( window, left_colour, right_colour, target_rect ):
    colour_rect = pygame.Surface( ( 2, 2 ) )
    pygame.draw.line( colour_rect, left_colour, ( 0,0 ), ( 0,1 ) )
    pygame.draw.line( colour_rect, right_colour, ( 1,0 ), ( 1,1 ) )
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )
    window.blit( colour_rect, target_rect )
while True:
    
    for udalost in pygame.event.get():
        if udalost.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'Game over'
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if keys[pygame.K_UP] and poz_Y2 > 0 :
        poz_Y2 -= rychlost2
    if keys[pygame.K_DOWN] and poz_Y2 < roz_Y - velikost :
        poz_Y2 += rychlost2
    if keys[pygame.K_LEFT] and poz_X2 > 0 :
        poz_X2 -= rychlost2
    if keys[pygame.K_RIGHT] and poz_X2 < roz_X - velikost :
        poz_X2 += rychlost2
        
        
    if keys[pygame.K_w] and poz_Y > 0 :
        poz_Y -= rychlost1
    if keys[pygame.K_s] and poz_Y < roz_Y - velikost :
        poz_Y += rychlost1
    if keys[pygame.K_a] and poz_X > 0 :
        poz_X -= rychlost1
    if keys[pygame.K_d] and poz_X < roz_X - velikost :
        poz_X += rychlost1
     
        
    if keys[pygame.K_RSHIFT] and boost2 > 0.3:
        rychlost2 *= 1.009
        boost2 -= 0.3
    if keys[pygame.K_RSHIFT] == False or boost2 < 0.4 :
        rychlost2 *= 0.99
        boost2 += 0.1
    if rychlost2 <= 1:
        rychlost2 = 1
    if rychlost2 >= 15:
        rychlost2 = 15
    if boost2 > 136:
        boost2 = 136



    if keys[pygame.K_LSHIFT] and boost1 > 0.3:
        rychlost1 *= 1.009
        boost1 -= 0.3
    if keys[pygame.K_LSHIFT] == False or boost1 < 0.4 :
        rychlost1 *= 0.99
        boost1 += 0.1
    if rychlost1 <= 1:
        rychlost1 = 1
    if rychlost1 >= 15:
        rychlost1 = 15
    if boost1 > 136:
        boost1 = 136
    
    okno.fill((192,192,192))
    c1 = circle(okno,(192,192,192),poz_X + velikost / 2,poz_Y + velikost / 2, velikost / 2 )
    c2 = circle(okno,(192,192,192),poz_X2 + velikost/ 2,poz_Y2 + velikost/ 2, velikost / 2)
    

    if c1.collidecircle(c2) == True and rychlost1 > 13 :
        rychlost1 = 1
        vykresleni2 = False
        rychlost2 = 0
        poz_X2 = roz_X / 1.5
        poz_Y2 = roz_Y / 2 - 50 
        time1 = time.time()
    if time.time() - time1 > 2:
        vykresleni2 = True 
        rychlost2 = 1
        time1 = 9999999999999999999999999999999999999999999999999
        
        
    if c1.collidecircle(c2) == True and rychlost2 > 13 :
        rychlost2 = 1
        vykresleni1 = False
        rychlost1 = 0
        poz_X = roz_X / 4
        poz_Y = roz_Y / 2 - 50
        time2 = time.time()
    if time.time() - time2 > 2:
        vykresleni1 = True 
        rychlost1 = 1
        time2 = 9999999999999999999999999999999999999999999999999999999
    if vykresleni2 == True :
        okno.blit( Ufo_red, (poz_X2,poz_Y2))

    if vykresleni1 == True :
        okno.blit( Ufo_blue, (poz_X,poz_Y))
    okno.blit(font.render(text, True, (0, 0, 0)), (roz_X / 2 - 60, 48)) 

    pygame.draw.rect(okno, (0,0,0), (roz_X - 280, roz_Y - 100, 140, 50),2)
    gradientRect( okno, (255, 255, 0), (255, 0, 0), pygame.Rect( roz_X - 278,roz_Y - 98, boost2, 46 ) )

    pygame.draw.rect(okno, (0,0,0), (140 ,roz_Y - 100, 140, 50),2)
    gradientRect( okno, (255, 255, 0), (255, 0, 0), pygame.Rect(142,roz_Y - 98, boost1, 46 ) )
    
    pygame.draw.rect(okno, (255,0,0), (roz_X - 7, roz_Y / 2 - 100,7,200 ))
    pygame.display.update()
    hodiny.tick(FPS)

