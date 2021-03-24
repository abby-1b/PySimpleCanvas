import pygame

screen = None
fill_color = (0, 0, 0)

def draw_init(_screen):
    global screen
    screen = _screen

def _color_process(c):
    if len(c) == 1:
        return (c[0], c[0], c[0])
    return tuple(c)

def fill(*c):
    fill_color = _color_process(c)

def background(*c):
    screen.fill(_color_process(c))

def circle(x, y, r):
    pygame.draw.circle(screen, fill_color, (x, y), r)

def rect(x, y, w, h):
    pygame.draw.rect(screen, fill_color, pygame.Rect(x, y, w, h))