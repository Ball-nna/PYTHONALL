import pgzrun

def draw():
    screen.clear()
    screen.draw.text('Program sound',center=(320,30),fontsize=40)
    screen.draw.text('1. alone_heart',(250,100),fontsize=36)
    screen.draw.text('2. alway',(250,150),fontsize=36)
    screen.draw.text('3. carrie',(250,200),fontsize=36)
    screen.draw.text('4. iithink',(250,250),fontsize=36)
    screen.draw.text('5. stop music',(250,300),fontsize=36)
    screen.draw.text('Select music : ',(220,350),fontsize=36)

def on_key_down(key,mod,unicode):
    if(key == keys.K_1):
        music.play_once('or')
    elif(key == keys.K_2):
        music.play_once('gas')
    elif(key == keys.K_3):
        music.play_once('carrie')
    elif(key == keys.K_4):
        music.play_once('i_think_i')

WIDTH=640
HEIGHT=480
pgzrun.go()
    
