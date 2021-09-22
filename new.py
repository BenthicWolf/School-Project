import pyglet

on = pyglet.image.load("on.png")
off = pyglet.image.load("off.png")

window = pyglet.window.Window(caption="My Window", fullscreen=True)
batch = pyglet.graphics.Batch()
fps_label = pyglet.window.FPSDisplay(window)
fps_label.label.batch = batch

label = pyglet.text.Label("Hello, World!", font_size=48, anchor_y="top", y=window.height, batch=batch)

button = pyglet.gui.PushButton(window.width//2, window.height//2, on, off, batch=batch)
window.push_handlers(button)

@window.event
def on_draw():
  window.clear()
  batch.draw()

@button.event
def on_press():
  print("Pressed!")

def update(dt: float):
  pass

pyglet.clock.schedule(update)
pyglet.app.run()