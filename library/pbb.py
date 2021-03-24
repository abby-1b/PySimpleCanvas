import pygame

from library.draw import *
from library.pbb_math import *
from library.sprite import *
from library.controller import *

import inspect

pygame.init()

keys_pressed = []
mouse_x, mouse_y, mouse_pressed = (0, 0, 0)
running = False
screen = None

def size(w=500, h=500, resizable=False):
    global screen
    if resizable:
        screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
    else:
        screen = pygame.display.set_mode((w, h))

    draw_init(screen)
    sprite_init(screen)

def name(n):
    pygame.display.set_caption(n)

def icon(n):
    pygame.display.set_icon(n)

def init():
    global running

    # Get globals (very hacky ;-;)
    g = dict(inspect.getmembers(inspect.stack()[1][0]))["f_globals"]

    # Setup some variables
    g["keys_pressed"] = []

    # Run setup
    g["setup"]()

    # Mouse Events
    if not "mouse_clicked" in g: g["mouse_clicked"] = (lambda *x: None)
    if not "key_pressed" in g: g["key_pressed"] = (lambda *x: None)
    if not "key_released" in g: g["key_released"] = (lambda *x: None)
    if not "window_resized" in g: g["window_resized"] = (lambda *x: None)

    # Run until the user asks to quit
    g["running"] = True
    clock = pygame.time.Clock()
    while g["running"]:
        #print(g["keysPressed"])

        if g["mouse_pressed"] != 0:
            g["mouse_pressed"] += 1

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g["running"] = False
            elif event.type == pygame.MOUSEMOTION:
                g["mouseX"], g["mouseY"] = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN:
                g["mouse_pressed"] = 1
            elif event.type == pygame.MOUSEBUTTONUP:
                if g["mouse_pressed"] < 300:
                    g["mouse_clicked"]()
                g["mouse_pressed"] = 0
            elif event.type == pygame.KEYDOWN:
                g["keys_pressed"] += [event.unicode]
                g["key_pressed"](event.unicode, event.key)
            elif event.type == pygame.KEYUP:
                g["keys_pressed"].remove(event.unicode)
                g["key_released"](event.unicode, event.key)
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                g["window_resized"](event.w, event.h)
            else:
                pass

        #print(clock.get_fps())
        g["loop"]()

        # Flip the display (vSync)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

class Object(object):
    def __getitem__(self, x):
        return getattr(self, x)
