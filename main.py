from mouse.mouse_control import MouseControl

directions_list = [[(1, 0), (0, 1), (0, 0), (1, 1), (2, 1), (2, 2), (1, 2), (0, 2)],
              [(3, 0), (2, 0), (1, 1), (2, 2), (2, 1), (1, 0), (0, 1), (1, 2)]
              ]

if __name__ == "__main__":
    mouse = MouseControl()
    mouse.prepare()
    for directions in directions_list:
        init_x, init_y = directions[0]
        print(init_x, init_y)
        mouse.goto(init_x, init_y)
        mouse.press()
        for d in directions:
            x, y = d
            mouse.goto(x, y)
        mouse.press()
