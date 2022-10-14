import itertools


candy_red = (255, 110, 135)
candy_orange = (255, 185, 105)
candy_blue = (0, 240, 225)
candy_purple = (125, 25, 250)


candy_colors = {
    'candy_orange':candy_orange,
    'candy_blue': candy_blue,
    'candy_purple': candy_purple,
    'candy_red': candy_red
    }

candy_colors_list = itertools.cycle([v for k, v in candy_colors.items()])
