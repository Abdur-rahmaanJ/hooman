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
    v = ((val - start) / (end-start)) * (realend-realstart)
    return realstart + v