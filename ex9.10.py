import pgzrun

def draw():
    screen.fill(bg_color)
    screen.draw.text('This is super File',(200,10),color='blue')
    apple.draw()
    apple1.draw()

def update():
    move_player()
    apple1.x +=0.5
    if apple1.x > WIDTH:
        apple1.x =0
def move_player():
    if (keyboard.LEFT):
        apple.x -= 15
    elif(keyboard.RIGHT):
        apple.x += 15
    if apple.x < apple.width/2:
        apple.x = apple.width/2
    elif apple.x > WIDTH-apple.width/2:
        apple.x =  WIDTH-apple.width/2
    if (keyboard.UP):
        apple.y -= 15
    elif(keyboard.DOWN):
        apple.y += 15
    if apple.y < apple.height/2:
        apple.y = apple.height/2
    elif apple.y > HEIGHT-apple.height/2:
        apple.y =  HEIGHT-apple.height/2

def on_key_down(key,mod,unicode):
    global bg_color
    if key == keys.R:
        bg_color = (255,0,0)
    if key == key.B:
        bg_color =(0,0,255)
    if key == key.G:
        bg_color =(0,255,0)
    if key == key.V:
        bg_color =(123,0,135)
    
def on_key_up(key,mod):
    pass
WIDTH =640
HEIGHT =480
apple= Actor('dor',(WIDTH/2,HEIGHT/2))
apple1= Actor('nobi',(WIDTH/2,HEIGHT/2))
bg_color=(0,0,255)
Play = False
pgzrun.go()
