new_sprite = None

import pygame

from library.draw import *
from library.pbb_math import *
from library.sprite_class import *
from library.controller import *

import inspect

pygame.init()

keys_pressed = []
mouse_x, mouse_y, mouse_pressed, mouse_time = (0, 0, 0, 0)

width, height = (500, 500)

running = False
frame_count = 0
screen = None

def size(w=500, h=500, resizable=False):
    w, h = int(w), int(h)
    g = dict(inspect.getmembers(inspect.stack()[1][0]))["f_globals"]

    g["width"], g["height"] = w, h
    global screen
    if resizable:
        screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
    else:
        screen = pygame.display.set_mode((w, h))

    draw_init(screen, new_sprite)

def name(n):
    pygame.display.set_caption(n)

def icon(n):
    pygame.display.set_icon(n)

def init():
    global running, screen

    # Get globals (very hacky ;-;)
    g = dict(inspect.getmembers(inspect.stack()[1][0]))["f_globals"]

    # Setup some variables
    g["keys_pressed"] = []

    # Run setup
    g["setup"]()

    g["screen"] = screen
    g["frame_count"] = 0

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
            g["mouse_time"] += 1

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g["running"] = False
            elif event.type == pygame.MOUSEMOTION:
                g["mouse_x"], g["mouse_y"] = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    g["mouse_pressed"] += 4
                else:
                    g["mouse_pressed"] += event.button
            elif event.type == pygame.MOUSEBUTTONUP:
                if g["mouse_time"] < 40:
                    g["mouse_clicked"]()
                g["mouse_time"] = 0
                if event.button == 3:
                    g["mouse_pressed"] -= 4
                else:
                    g["mouse_pressed"] -= event.button
            elif event.type == pygame.KEYDOWN:
                g["keys_pressed"] += [event.unicode]
                g["key_pressed"](event.unicode, event.key)
            elif event.type == pygame.KEYUP:
                g["keys_pressed"].remove(event.unicode)
                g["key_released"](event.unicode, event.key)
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                g["window_resized"](event.w, event.h)
                g["width"], g["height"] = event.w, event.h
            else:
                pass

        #print(clock.get_fps())
        g["loop"]()

        # Flip the display (vSync)
        pygame.display.flip()
        clock.tick(60)
        
        g["frame_count"] += 1
    pygame.quit()

class Object(object):
    def __getitem__(self, x):
        return getattr(self, x)
