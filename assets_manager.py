import pygame.image

class Assets_manager():
    def __init__(self):
        self._images = []
        self._sounds = [()]
        self._rootpath = ""

    def set_root(self, path):
        self._rootpath = path

    def load_images(self, paths):
        for p in paths:
            self._images.append((p[0] ,pygame.image.load(self._rootpath + p[1]).convert()))

    def get_image(self, name):
        for i in self._images:
            if(i[0] ==  name):
                return i[1]

