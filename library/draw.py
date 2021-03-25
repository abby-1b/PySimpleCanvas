import pygame
from math import pi
import library.sprite_class as sprite_class

_screen = None
fill_color = [0, 0, 0]
translation = [0, 0]
new_sprite = None

pygame.font.init()
_font = pygame.font.SysFont(pygame.font.get_default_font(), 36)

def draw_init(__screen, __new_sprite):
    global _screen, new_sprite
    _screen = __screen
    new_sprite = __new_sprite

def _color_process(c):
    if type(c[0]) in [list, tuple]: c = c[0]
    if type(c) == tuple: c = list(c)
    if type(c) in [float, int]: c = [c]
    if len(c) == 1:
        return [c[0], c[0], c[0], 255]
    elif len(c) == 2:
        return [c[0], c[0], c[0], c[1]]
    elif len(c) == 3:
        return c + [255]
    return c

# Functions
def translate(x, y):
    translation[0] += x
    translation[1] += y

def fill(*c):
    global fill_color
    fill_color = _color_process(c)

def text(t, x, y, surface=None):
    if surface == None: surface = _screen
    _text = _font.render(str(t), False, (0, 0, 0))
    surface.blit(_text, pygame.Rect(x, y, _text.get_width(), _text.get_height()))

def background(*c, surface=None):
    if surface == None: surface = _screen
    if hasattr(surface, '_fill'):
        surface._fill(_color_process(c))
    else:
        surface.fill(_color_process(c))

def circle(x, y, r, surface=None):
    if surface == None: surface = _screen
    pygame.draw.circle(surface, fill_color, (x + translation[0], y + translation[1]), r)

def rect(x, y, w, h, surface=None):
    if surface == None: surface = _screen
    pygame.draw.rect(surface, fill_color, pygame.Rect(x + translation[0], y + translation[1], w, h))

# Sprites
def load_sprite(name=None):
    """Loads an image from the filesystem and returns it.

    Args:

        name (str): Image name

    Returns:

        Image: the loaded image.
    """
    return sprite_class.new_sprite(pygame.image.load(name))

def sprite(image, x, y=None, surface=None, center=False, rotation=0):
    """Draws a sprite to the screen using XY coordinates.

    Args:

        image (Image): The sprite to be drawn
        x (float): The X position of the sprite
        y (float): The Y position of the sprite
    """
    if surface == None: surface = _screen

    if rotation != 0:
        image = pygame.transform.rotate(image, rotation * (180 / pi))

    if y == None:
        y = x[1]
        x = x[0]
    if center:
        x -= image.get_width() / 2
        y -= image.get_height() / 2

    surface.blit(image, pygame.Rect(x + translation[0], y + translation[1], image.get_width(), image.get_height()))

def fast_sprite(image, p, surface=None):
    if surface == None: surface = _screen
    surface.blit(image, pygame.Rect(p[0] + translation[0], p[1] + translation[1], image.get_width(), image.get_height()))