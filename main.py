import os
import pygame
from pygame import *
from entities.background import Background
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
        self._objects = []
 
    def on_init(self):
        # pylint: disable=no-member
        pygame.init()
        pygame.display.set_caption('Test')
        # pylint: disable=no-member
        self._display_surf = pygame.display.set_mode(self.size, pygame.constants.HWSURFACE | pygame.constants.DOUBLEBUF)
        back = Background()
        back.set_image(os.path.join('D:/Programming/Python/PyKetBall/assets', 'background.png'))
        self._objects.append(back)
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.constants.QUIT:
            self._running = False
    def on_loop(self):
        pass
    def on_render(self):
        self._objects[0].draw(self._display_surf)
        pygame.display.flip()
        pass
    def on_cleanup(self):
        # pylint: disable=no-member
        pygame.quit()
        # pylint: disable=no-member
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()