import os
import pygame

from pygame import *
from entities.background import Background
from entities.player import Player
from assets_manager import Assets_manager

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 800, 600
        self._assets_manager = Assets_manager()
        self._objects = []

    def on_init(self):
        # pylint: disable=no-member
        pygame.init()
        pygame.display.set_caption('PyKetBall')
        # pylint: disable=no-member

        self._display_surf = pygame.display.set_mode(self.size, pygame.constants.HWSURFACE | pygame.constants.DOUBLEBUF)
        
        self._assets_manager.load_assets()

        bak = Background()
        bak.set_image(self._assets_manager.get_image("background"))
        bak.set_size(self._display_surf.get_width(), self._display_surf.get_height())

        player = Player()
        player.set_image(self._assets_manager.get_image("player"))
        player.set_position(100,100)
        player.set_size(int(self._display_surf.get_width() / 10), int(self._display_surf.get_height() / 3))

        self._objects.append(bak)
        self._objects.append(player)
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.constants.QUIT:
            self._running = False
    def on_loop(self):
        pass
    def on_render(self):

        for o in self._objects:
            o.draw(self._display_surf)

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