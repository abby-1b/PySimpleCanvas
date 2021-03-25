class new_sprite(pygame.Surface):
    def __init__(self, w, h=None):
        if h == None:
            super().__init__((w.get_width(), w.get_height()), pygame.SRCALPHA, 32)
            self.blit(w, pygame.Rect(0, 0, w.get_width(), w.get_height()))
        else:
            super().__init__((w, h), pygame.SRCALPHA, 32)
        self._fill = super().fill
        self.translation = [0, 0]
        self.fill_color = (0, 0, 0)
    
    def rotated(self, a):
        return new_sprite(pygame.transform.rotate(self, a))
    
    def scale(self, t):
        return new_sprite(pygame.transform.scale(self, (self.get_width() * t, self.get_height() * t)))
