import pygame.image

resource_file = "assets/assets.res"

class Assets_manager():
    def __init__(self):
        self._images = []
        self._sounds = [()]
        self._rootpath = "assets/"

    def set_root(self, path):
        self._rootpath = path

    def load_images(self, name, path):
        self._images.append((name ,pygame.image.load(self._rootpath + path).convert_alpha()))

    def get_image(self, name):
        for i in self._images:
            if(i[0] ==  name):
                return i[1]

    def load_assets(self):
        f = open(resource_file, "r")
        for s in f:
            splitted = s.split(' ')
            self.load_images(splitted[0], splitted[1].strip())
        f.close()
