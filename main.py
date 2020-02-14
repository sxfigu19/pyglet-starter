import pyglet
win = pyglet.window.Window()

label = pyglet.text.Label('Hello, Player!', font_size=22, x = 250, y = 450)
labeltwo = pyglet.text.Label('Hope you are ready', font_size=17, x = 235, y = 420)
labelthree = pyglet.text.Label('Enjoy the game!', font_size=12, x = 275, y = 395)

# Create a sprite so the game can keep track of coordinates
img= pyglet.image.load('assets/hero/sliced/surprise.png')
spr1 = pyglet.sprite.Sprite(img, x = 350, y = 250,)
pic= pyglet.image.load('assets/hero/sliced/surprise.png')
spr2 = pyglet.sprite.Sprite(pic, x = 300, y = 250)

# Get the key state handler object
keys = pyglet.window.key.KeyStateHandler()

def update(dt):
    win.push_handlers(keys) # update the key object
    if keys[pyglet.window.key.SPACE]:
        print("Spacebar pressed!")
    if keys[pyglet.window.key.UP]:
        print("Up key pressed!")

@win.event
def on_draw():
    win.clear()
    #img.blit(200, 100)
    label.draw()
    labeltwo.draw()
    labelthree.draw()
    spr1.draw()
    spr2.draw()

pyglet.clock.schedule(update) 
pyglet.app.run()
