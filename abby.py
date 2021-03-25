## This is the shit i do. don't fucken touch it.
from library.pbb import *

yellow = (226, 230, 168)
purple = (63, 63, 116)

stage = new_sprite(1920 * 2, 1080 * 2)

player = Object()
player.pos = [250, 250]
player.vel = [0, 0]
player.sprite = load_sprite("Assets/ship.png")

def setup():
    size(1920 / 2, 1080 / 2, resizable=True)
    name("Rocket!")

    stage.background(purple)
    stage.fill(0, 0, 0, 0)

    stage.translate(20, 20)

def loop():
    background(random() * 255)

    stage.circle(mouse_x, mouse_y, 20)
    sprite(stage, 0, 0)

def window_resized(w, h):
    global stage

init()
