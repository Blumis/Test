import pygame
import sys
import math
import random





pygame.init()

screen = pygame.display.set_mode((1280, 720))


black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

width, height = screen.get_size()




x  = 0
y = 0
angle = -90
angle2 = 45
angle3 = 60
#stala dlugosc linii
r = 200
r2 = r/2
r3=r2/2
#ilosc platkow rozy, jesli parzysta to platki = 2k
k=5        
vel = 0.5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit(0)

    
    #if pygame.key.get_pressed()[pygame.K_a]:
        #angle-=1
    #if pygame.key.get_pressed()[pygame.K_d]:
        #angle+=1
    #if pygame.key.get_pressed()[pygame.K_w]:
        #r+=1
    #if pygame.key.get_pressed()[pygame.K_s]:
        #r-=1


    angle += vel
    
    angle2 -= 2*vel
     
    angle3 += 3*vel
    
    rads2 = math.radians(angle2)
    
    rads3 = math.radians(angle3)
    
    rads = math.radians(angle)      #radian = kat
    
    #r = 50*(5*math.cos(k*rads+2))   #wzor na rysowanie rozy

    x = width/2+r*math.cos(rads)
    y = height/2+r*math.sin(rads)

    x2 = x+r2*math.cos(rads2)
    y2 = y+r2*math.sin(rads2)
    
    x3 = x2+r3*math.cos(rads3)
    y3 = y2+r3*math.sin(rads3)


 
    screen.fill(black)
    
    pygame.draw.line(screen,white,(width/2,height/2),(x,y),1)
    pygame.draw.line(screen,white,(x,y),(x2,y2),1)
    pygame.draw.line(screen,white,(x2,y2),(x3,y3),1)
    pygame.draw.circle(screen, red, [int(x), int(y)], 5, 0)
    pygame.draw.circle(screen, green, [int(x2), int(y2)], 5, 0)
    pygame.draw.circle(screen, blue, [int(x3), int(y3)], 5, 0)
                 


  
    
    pygame.display.flip()
