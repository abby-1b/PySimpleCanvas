import pygame

screen = None

def sprite_init(_screen):
    global screen
    screen = _screen

def load_image(name):
    """Loads an image from the filesystem and returns it.

    Args:

        name (str): Image name

    Returns:

        Image: the loaded image.
    """    
    return pygame.image.load(name)

def sprite(image, x, y=None):
    """Draws a sprite to the screen using XY coordinates

    Args:

        image (Image): The sprite to be drawn
        x (float): The X position of the sprite
        y (float): The Y position of the sprite
    """
    if y == None:
        screen.blit(image, pygame.Rect(x[0], x[1], image.get_width(), image.get_height()))
    else:
        screen.blit(image, pygame.Rect(x, y, image.get_width(), image.get_height()))