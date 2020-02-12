import pyglet
window = pyglet.window.Window()

label = pyglet.text.Label('Hello, Player!',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
@window.event
def on_draw():
    win.clear()
    img.blit(200, 100)
    # spr.draw()

pyglet.clock.schedule(update) 
pyglet.app.run()
