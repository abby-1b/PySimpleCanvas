# Import the library
from library.pbb import *

# Defines some colors. All colors are defined as tuples or lists.
yellow        = (226, 230, 168)
purple        = (63, 63, 116)

# The stage itself is just a sprite the size of the screen.
stage         = new_sprite(1920 / 2, 1080 / 2)

# Defines the player as an object with a position, velocity and a sprite.
# This is way easier than using a dict, at the cost of speed.
player        = Object()
player.pos    = [0, 19, 0] # X position, Y position, angle
player.vel    = [0, 0, 0]
player.sprite = load_sprite("Assets/ship.png"  ).scale(2)

# This is the setup function. It runs once before the loop function.
def setup():
    # Instances the screen as resizable, meaning its corners can be dragged.
    size(1920 / 2, 1080 / 2, resizable=True)
    
    # Sets the window's name
    name("PySimpleGame Example")

    # Draws a purple rectangle that acts as 'ground' for the player's ship.
    stage.fill(purple)
    stage.rect(0, stage.height / 2, 
               stage.width, stage.height / 2)

# This is the loop function. It runs every single frame.
def loop():
    # Draw background color
    background(yellow)

    # moves the origin (x 0, y 0) to the center of the screen
    translate(width / 2, height / 2)
    
    # Draws the stage quickly. The `fast_sprite` method has 
    # less functionality (no rotation, no centering) than 
    # the `sprite` method, but is a bit faster.
    fast_sprite(stage, (-stage.width / 2 + player.pos[0], 
                        -stage.height / 2 - player.pos[1]))
    
    # Draws the player sprite, centered and rotated.
    sprite(player.sprite, 0, 0, center=True, rotation=player.pos[2])

    # `keys_pressed` contains a list of all the keys that are
    # currently pressed. This list updates every frame
    # when a key is pressed or released.
    
    # This controls the player's ship by simulating two burners,
    # used for both rotating the ship and accelerating forward.
    if "a" in keys_pressed:
        player.vel[2] += 0.005
        player.vel[0] += cos(player.pos[2] - pi / 2) * 0.4
        player.vel[1] += sin(player.pos[2] - pi / 2) * 0.4
    if "d" in keys_pressed:
        player.vel[2] -= 0.005
        player.vel[0] += cos(player.pos[2] - pi / 2) * 0.4
        player.vel[1] += sin(player.pos[2] - pi / 2) * 0.4
    # NOTE: these two letters can be pressed simultaneously, so an `elif` here
    # would only allow you to press one button at a time, prioritizing 'a'.

    # Increments the Y velocity (making the player
    # accelerate down, hence simulating 'gravity').
    player.vel[1] += 0.1
    
    # Updates the player's speed as part of the `controller` submodule.
    update_speed(player, friction=0.99, v_friction=True)
    
    # Caps the player's up/down velocity.
    player.vel[2] *= 0.95

# This function is called every time the window is resized.
# However, it is not used here for some reason.
def window_resized(w, h):
    global stage

# Remember to call `init` to start the library
# after declaring the setup and loop functions!
init()
