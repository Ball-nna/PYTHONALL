import pgzrun
import random

def draw():
    #screen.fill('white')
    screen.blit('uni',(0,0))
    screen.draw.text('Rotation image',(200,20),color='blue')
    screen.draw.text('Rotation angle :'+str(apple.angle),(50,400),color='blue')
    apple.draw()

def update():
    apple.angle += 1
    if(apple.angle == 360):
        apple.angle = 0
    apple.x -= 1
    if apple.x ==0:
        apple.x= WIDTH

#main

WIDTH = 640
HEIGHT = 480
apple = Actor('ชช')
apple.pos = (WIDTH/2,HEIGHT/2)
#apple.anchor =(0,0)
pgzrun.go()
    
