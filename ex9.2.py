import pgzrun

def draw():
    screen.fill('white')
    screen.draw.text('Change Position and Display',topleft=(150,80),color='blue')
    logo.draw()

def update():
    if (logo.x < WIDTH):
        logo.x += 2
    if (logo.y < HEIGHT):
        logo.y += 2

WIDTH = 1000
HEIGHT = 1000
logo = Actor('it_logo',(0,0))
pgzrun.go()
