import pygame

_screen = None
fill_color = [0, 0, 0]
translation = [0, 0]

def draw_init(__screen):
    global _screen
    print("Previous screen:", _screen)
    _screen = __screen

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
    print(fill_color)

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
    return pygame.image.load(name)

def sprite(image, x, y=None, surface=None):
    """Draws a sprite to the screen using XY coordinates.

    Args:

        image (Image): The sprite to be drawn
        x (float): The X position of the sprite
        y (float): The Y position of the sprite
    """
    if surface == None: surface = _screen
    if y == None:
        surface.blit(image, pygame.Rect(x[0] + translation[0], x[1] + translation[1], image.get_width(), image.get_height()))
    else:
        surface.blit(image, pygame.Rect(x + translation[0], y + translation[1], image.get_width(), image.get_height()))
