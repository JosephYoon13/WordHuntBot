import mouse.mouse_emulate as me

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

    def goLeft(self):
        self.client.state = [int(self.pressed), 244, 0, 0]
        self.client.send_current()
        self.client.state = [int(self.pressed), 0, 0, 0]
    
    def goUp(self):
        self.client.state = [int(self.pressed), 0, 244, 0]
        self.client.send_current()
        self.client.state = [int(self.pressed), 0, 0, 0]
    
    def goRight(self):
        self.client.state = [int(self.pressed), 12, 0, 0]
        self.client.send_current()
        self.client.state = [int(self.pressed), 0, 0, 0]
    
    def goDown(self):
        self.client.state = [int(self.pressed), 0, 12, 0]
        self.client.send_current()
        self.client.state = [int(self.pressed), 0, 0, 0]

    def prepare(self):
        self.client.state = [0, 1, 0, 0]
        self.client.send_current()
        self.client.state = [0, 255, 0, 0]
        self.client.send_current()
        self.client.state = [0, 238, 0, 0]
        self.client.send_current()
        self.client.state = [0, 0, 226, 0]
        self.client.send_current()


    def goto(self, new_x, new_y):
        xdif = self.x_curr - new_x
        ydif = self.y_curr - new_y

        dx = abs(xdif)
        dy = abs(ydif)

        while (dx > 0 or dy > 0):
            if (ydif < 0):
                self.goRight
            if (ydif > 0):
                self.goLeft()
            if (xdif > 0):
                self.goUp()
            if (xdif < 0):
                self.goDown()
            dx -= 1
            dy -= 1

        self.x_curr = new_x
        self.y_curr = new_y

    