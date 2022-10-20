
import io


from hooman import Hooman


window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)


def string_to_file(string):
    import tempfile
    file_like_object = tempfile.NamedTemporaryFile()
    file_like_object.write(string.encode())
    file_like_object.flush()
    return file_like_object

while hapi.is_running:
    bg_col = (255, 255, 255)
    hapi.background(bg_col)

    with open('/home/appinv/code/hooman/hooman/lucide/activity.svg') as f:
        f = string_to_file(f.read())
        surface = hapi.pygame.image.load(f)

    hapi.screen.blit(surface, (0, 0))


    hapi.flip_display()
    hapi.event_loop()
