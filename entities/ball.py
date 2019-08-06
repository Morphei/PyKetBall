from entity import Entity

class Ball(Entity):
    def _init__(self):
        super.__init__()

    def mouse_down(self):
        pass
    
    def mouse_up(self):
        pass
    
    def send_event(self, event):
        super.update(event)
        if(event.type == pygame.MOUSEBUTTONUP):
            mouse_up()
        if(event.type == pygame.MOUSEBUTTONDOWN):
            mouse_down()
