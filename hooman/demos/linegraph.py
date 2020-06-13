from hooman import Hooman


window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)


ctest = [10, 20]

while hapi.is_running:
    bg_col = (255, 255, 255)
    hapi.background(bg_col)

    hapi.linechart(40, 30, 300, 200, {'data':[[0, 0], [10, 10], [20, 20], [30, 30], [90,20]],
        'mouse_line':True,
        'range_y':[0, 200],
        'range_x':[0, 300],})
    hapi.fill(hapi.color['blue'])
    x1 = 40 + (10/100)*300
    y1 = 30 + (100/200 * 20)

    hapi.ellipse(x1, y1, 10, 10)
    #hapi.text(hapi.mouseX(), 200, 200)
    # print(hapi.mouseX(), hapi.mouseY())
    hapi.flip_display()
    hapi.event_loop()

