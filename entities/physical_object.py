from entity import Entity

class Physical_object(Entity):
    def __init__ (self):
        Entity.__init__(self)
        self._gravity = 5
        self._acceleration_x = 0
        self._acceleration_y = 0
        self._on_surface = False

    def update(self):
        Entity.update(self)

        if self._on_surface == False:
            self._y += 1
        pass
    
    def set_acceleration(self, vector_x, vector_y):
        print(vector_x, vector_y)
        pass
        
    