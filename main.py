import pyglet
from util import *

win = pyglet.window.Window()
# Load the image & create the sprite
img = pyglet.image.load('assets/hero/Old hero.png')
spr = pyglet.sprite.Sprite(img, x = 100, y = 200)


def update(dt):
  pass

@win.event
def on_draw():
  win.clear()
  # pixelScale()

  spr.draw()

pyglet.clock.schedule(update)
pyglet.app.run()

