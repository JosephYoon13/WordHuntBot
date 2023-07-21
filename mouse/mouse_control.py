import mouse_emulate as me

class MouseControl:
    def __init__(self):
        self.x_curr = 0
        self.y_curr = 0
        self.pressed = 0
        self.client = me.MouseClient()
        self.client.state = [0, 0, 0, 0]
        for i in range(10):
            self.client.send_current()

    def press(self):
        if self.pressed:
            self.pressed = 0
        else:
            self.pressed = 1
    

    