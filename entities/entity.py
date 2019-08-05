import pygame.display

class Entity():
    def __init__ (self):
        self._x = 0
        self._y = 0
        self._width = 0
        self._heigth = 0
    
    def set_image(self, path):
        self._image = pygame.image.load(path).convert()

    def draw(self, display):
        display.blit(self._image, (self._x, self._y))