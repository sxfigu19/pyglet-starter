import pyglet

win= pyglet.window.Window()

# Create a sprite so the game can keep track of coordinates
img= pyglet.image.load('assets/hero/sliced/surprise.png')
spr = pyglet.sprite.Sprite(img, x = 200, y = 200)

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
    spr.draw()

pyglet.clock.schedule(update) 
pyglet.app.run()