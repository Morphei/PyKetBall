import pygame.display

class Entity():
    def __init__ (self):
        self._x = 0
        self._y = 0
        self._origin_width = 0
        self._origin_height = 0
        self._width = 0
        self._heigth = 0
    
    def set_image(self, image):
        self._image = image.convert_alpha()
        self._scaled_image = image
        self._origin_height = image.get_height()
        self._origin_width = image.get_width()
        self._heigth = self._origin_height
        self._width = self._origin_width

    def get_image(self):
        return self._scaled_image

    def draw(self, display):
        display.blit(self._scaled_image, (self._x, self._y))

    def set_position(self, x, y):
        self._x = x
        self._y = y

    def set_size(self, w, h):
        self._scaled_image = pygame.transform.scale(self._image, (w, h))
        self._width = w
        self._heigth = h

    def scale(self, scale_factor):
        self._scaled_image = pygame.transform.scale(self._image, (int(self._origin_width * scale_factor), int(self._origin_height * scale_factor)))

    def get_size(self):
        return (self._width, self._heigth)

    def update(self):
        pass

    def send_event(self, event):
        pass

    def collide(self, image):
        return self._image.get_rect().colliderect(image.get_rect())