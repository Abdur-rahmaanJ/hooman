from hooman import Hooman

hapi = Hooman(500, 500)

tb = hapi.text_box(10, 10, 100, params={"background_color": (100, 100, 100)})

while hapi.is_running:
    hapi.background(hapi.color['white'])
    tb.update()

    hapi.flip_display()
    hapi.event_loop()