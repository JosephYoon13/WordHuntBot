import mouse.mouse_emulate as me
import time

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
        self.client.state = [int(self.pressed), 0, 0, 0]
        self.client.send_current()

    def prepare(self):
        self.client.state = [0, 1, 0, 0]
        self.client.send_current()
        self.client.state = [0, 255, 0, 0]
        self.client.send_current()
        self.client.state = [0, 238, 0, 0]
        self.client.send_current()
        self.client.state = [0, 0, 226, 0]
        self.client.send_current()
        self.client.state = [int(self.pressed), 0, 0, 0]
        self.client.send_current()

    def goto(self, new_x, new_y):
        xdiff = self.x_curr - new_x
        ydiff = self.y_curr - new_y
        dx = abs(xdiff)
        dy = abs(ydiff)
        while dx > 0 or dy > 0:
            if dx > 0:
                if xdiff > 0:
                    self.client.state = [int(self.pressed), 0, 224, 0]
                    self.client.send_current()
                else:
                    self.client.state = [int(self.pressed), 0, 12, 0]
                    self.client.send_current()
            if dy > 0:
                if ydiff > 0:
                    self.client.state = [int(self.pressed), 224, 0, 0]
                    self.client.send_current()
                else:
                    self.client.state = [int(self.pressed), 12, 0, 0]
                    self.client.send_current()
            dx -= 1
            dy -= 1
        self.x_curr = new_x
        self.y_curr = new_y
        time.sleep(3)

    def move(self, new_x, new_y):
        dx = 12
        dy = 12

        if new_x <= self.x_curr:
            dx = 224
            if new_x == self.x_curr:
                dx = 0     

        if new_y <= self.y_curr:
            dy = 224
            if new_y == self.y_curr:
                dy = 0

        self.x_curr = new_x
        self.y_curr = new_y
        self.client.state = [int(self.pressed), dy, dx, 0]
        self.client.send_current()
        time.sleep(3)




    