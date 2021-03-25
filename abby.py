## This is the shit i do. don't fucken touch it.
from library.pbb import *

yellow = (226, 230, 168)
purple = (63, 63, 116)

stage = new_sprite(1920 / 2, 1080 / 2)

player = Object()
player.pos = [0, 19, 0] # X, Y, angle
player.vel = [0, 0, 0]  # X, Y, angle
player.sprite = load_sprite("Assets/ship.png").scale(2)
player.burner = load_sprite("Assets/burner.png").scale(2)

def setup():
    size(1920 / 2, 1080 / 2, resizable=True)
    name("Rocket!")

    stage.fill(purple)
    stage.rect(0, stage.height / 2, stage.width, stage.height / 2)

def loop():
    background(yellow)

    translate(width / 2, height / 2)
    fast_sprite(stage, (-stage.width / 2 + player.pos[0], -stage.height / 2 - player.pos[1]))
    sprite(player.sprite, 0, 0, center=True, rotation=player.pos[2])

    draw_burner = 0
    if "a" in keys_pressed:
        player.vel[2] += 0.005
        draw_burner |= 1

        player.vel[0] += cos(player.pos[2] - pi / 2) * 0.4
        player.vel[1] += sin(player.pos[2] - pi / 2) * 0.4
    
    if "d" in keys_pressed:
        player.vel[2] -= 0.005
        draw_burner |= 2

        player.vel[0] += cos(player.pos[2] - pi / 2) * 0.4
        player.vel[1] += sin(player.pos[2] - pi / 2) * 0.4

    if draw_burner:
        sprite(player.burner, 0, 0, center=True, rotation=player.pos[2])

    player.vel[1] += 0.1
    update_speed(player, friction=0.99, v_friction=True)
    player.vel[2] *= 0.95

def window_resized(w, h):
    global stage

init()
