## This is the shit i do. don't fucken touch it.
from library.pbb import *

player = Object()
player.pos = [250, 250]
player.vel = [0, 0]
player.sprite = load_image("image.png")

def setup():
    size(500, 500, resizable=True)
    name("Game!")
    icon(load_image("image.png"))

def loop():
    background(255)
    control_2d_WASD(player)
    sprite(player.sprite, add(player.pos, [0, mouse_pressed]))

def window_resized(w, h):
    print(w, h)

init()
