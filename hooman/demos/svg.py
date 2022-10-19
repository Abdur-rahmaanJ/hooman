
import io


from hooman import Hooman


window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)


while hapi.is_running:
    bg_col = (255, 255, 255)
    hapi.background(bg_col)

    with open('/home/appinv/code/hooman/hooman/lucide/activity.svg', encoding='utf8') as f:
        f = io.BytesIO(bytes(f.read()), encoding='utf8')
        surface = hapi.pygame.image.load(f)

    hapi.screen.blit(surface, (0, 0))


    hapi.flip_display()
    hapi.event_loop()
