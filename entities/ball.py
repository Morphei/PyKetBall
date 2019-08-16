import pygame
from entity import Entity
from physical_object import Physical_object

class Ball(Physical_object):
    def _init__(self):
        Physical_object.__init__(self)
        self._mouse_down_coordinates(0,0)

    def mouse_down(self, event):
        self._mouse_down_coordinates = pygame.mouse.get_pos()
        pass
    
    def mouse_up(self, event):
        current_coordinates = pygame.mouse.get_pos()
        self.set_acceleration(self._mouse_down_coordinates[0] - current_coordinates[0], self._mouse_down_coordinates[1] - current_coordinates[1])
        pass
    
    def send_event(self, event):
        if(event.type == pygame.MOUSEBUTTONUP):
            self.mouse_up(event)
        if(event.type == pygame.MOUSEBUTTONDOWN):
            self.mouse_down(event)

    def update(self):
        Physical_object.update(self)

    def collide(self, image):
        if Physical_object.collide(self, image):
            self._on_surface = True
    