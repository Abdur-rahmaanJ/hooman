import math
import colorsys


def constrain(val, start, end, realstart, realend):
    # mouseX 0 width 0 255
    # v = (mouseX / (end-start)) * (realend-realstart)
    # return realstart + v
    # if val < start, val = start
    # if val > end, val = end

    if val < start:
        return start
    if val > end:
        return end
    v = ((val - start) / (end - start)) * (realend - realstart)
    return realstart + v


def round_to_num(x, base=1):
    return base * round(x / base)


def distance(coord1, coord2):
    x1 = coord1[0]
    y1 = coord1[1]
    x2 = coord2[0]
    y2 = coord2[1]
    squared_sums = math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)
    d = math.pow(squared_sums, 0.5)
    return d


def rgb_to_hls(r, g, b):
    r, g, b = [x / 255.0 for x in (r, g, b)]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return h, l, s


def hls_to_rgb(h, l, s):
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    r, g, b = [x * 255.0 for x in (r, g, b)]
    return r, g, b
