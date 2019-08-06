class Physical_object():
    def __init__ (self):
        self._gravity = 5
        self._acceleration_x = 0
        self._acceleration_y = 0
        self._on_surface = True

    def update(self):
        pass
    
    def set_acceleration(self, vector_x, vector_y):
        print(vector_x, vector_y)
        pass
        
    