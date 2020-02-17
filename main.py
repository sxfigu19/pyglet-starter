import pyglet
import util
win = pyglet.window.Window()

label = pyglet.text.Label('Hello, Player!', font_size=22, x = 250, y = 450)
labeltwo = pyglet.text.Label('Hope you are ready', font_size=17, x = 235, y = 420)
labelthree = pyglet.text.Label('Click the arrow keys to move your person', font_size=12, x = 190, y = 395)


cave= pyglet.image.load('assets/forest-assets/cave.png')
spr1 = pyglet.sprite.Sprite(cave, x = 80, y = 0)
spr1.scale = 10

# Create a sprite so the game can keep track of coordinates
img= pyglet.image.load('assets/hero/sliced/surprise.png')
spr2 = pyglet.sprite.Sprite(img, x = 150, y = 20,)
spr2.scale = 10


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
    util.pixelScale()
    win.clear()
    #img.blit(200, 100)
    label.draw()
    labeltwo.draw()
    labelthree.draw()
    spr1.draw()
    spr2.draw()

pyglet.clock.schedule(update)
pyglet.app.run()

