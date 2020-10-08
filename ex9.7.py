import pgzrun

def draw():
    screen.fill('white')
    screen.draw.text('Show get key',(200,10),color='blue')

def on_key_down(key,mod,unicode):
    print('Key Down :',key,unicode,mod)

def on_key_up(key,mod):
    print('Key up :',key,mod)
   

WIDTH = 640
HEIGHT = 480
pgzrun.go()
