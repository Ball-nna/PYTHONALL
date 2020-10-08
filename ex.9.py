import pgzrun

def draw():

   screen.fill('white')
   logo.draw()
   screen.draw.text('Load and Display image',(150,270),fontsize = 28,color='red')
   screen.draw.text('image Width : %d'%logo.width,(250,150),fontsize=24,color='blue')
   screen.draw.text('image height :%d'%logo.height,(250,200),fontsize=24,color='blue')

#main

WIDTH = 400
HEIGHT = 300
Name = 'it_logo'
logo = Actor(Name,(0,0))
rose = Actor('rose',(0,0))
pgzrun.go()
