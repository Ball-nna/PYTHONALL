import pgzrun

def draw():
    screen.fill(('black'))
    screen.draw.text('Show animate start(p) and stop(s)',(200,10),color='blue')
    apple.draw()
'''
def update():
    if Play:
       rose.x +=1
       if(rose.x > WIDTH):
            rose.x=0
            
def on_key_down(key,mod,unicode):
    global Play
    if(key == keys.P):
        Play = True
    elif(key == keys.S):
        Play = False
'''
def on_key_down(key,mod,unicode):
    if(key==keys.LEFT):
        apple.x -= 15
    elif(key==keys.RIGHT):
        apple.x +=15
    if(key==keys.DOWN):
        apple.y += 15
    if(key==keys.UP):
        apple.y -= 15
def on_key_up(key,mod):
    pass
              
WIDTH =640
HEIGHT =480
apple= Actor('apple',(WIDTH/2,HEIGHT/2))
Play = False
pgzrun.go()
