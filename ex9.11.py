import pgzrun

def draw():
    screen.clear()
    screen.draw.text('Program sound',(200,10),fontsize=40)
    screen.draw.text('1. bird',(250,50),fontsize=36)
    screen.draw.text('2. bug',(250,90),fontsize=36)
    screen.draw.text('3. dog',(250,130),fontsize=36)
    screen.draw.text('4. droid',(250,170),fontsize=36)
    screen.draw.text('5. duck',(250,210),fontsize=36)
    screen.draw.text('Select sound : ',(220,250),fontsize=36)

def on_key_down(key,mod,unicode):
    if(key == keys.K_1):
        sounds.bird.play()
    elif(key == keys.K_2):
        sounds.bug.play()
    elif(key == keys.K_3):
        sounds.dog.play()
    elif(key == keys.K_4):
        sounds.droid.play()
    elif(key == keys.K_5):
        sounds.duck.play()

WIDTH=640
HEIGHT=480
pgzrun.go()
    
