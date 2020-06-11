

def barchart(hapi, x, y, w, h, params):
    options = {
        'ticks_y':10,
        'tick_size':5,
        'range_y':[0, 100],
        'data':{'a':10, 'b':20},
        'bin_color':(255,99,97),
        'line_color':(200, 200, 200),
        'text_color': (100, 100, 100)
    }
    options.update(params)
    hapi.stroke_size(2)
    hapi.stroke(options['line_color'])
    hapi.line(x, y, x, y+h)
    hapi.line(x, y+h, x+w, y+h)
    hapi.fill(options['text_color'])
    y_top_val = options['range_y'][1]
    for t in range(options['ticks_y']):
        hapi.line(x, y+(t*(h//options['ticks_y'])), x-options['tick_size'], y+(t*(h//options['ticks_y'])))
        hapi.text(y_top_val, x-20, y+(t*(h//options['ticks_y']))-10)
        y_top_val -= (options['range_y'][1] - options['range_y'][0]) // options['ticks_y']

    num_data = len(options['data'].keys())
    divs = 1 + 1 + (num_data*2) + (num_data-1)
    space_unit = w//divs
    current_x = x + space_unit
    for i,d in enumerate(options['data']):
        hapi.fill(options['bin_color'])
        bin_height = hapi.constrain(
            options['data'][d], options['range_y'][0], options['range_y'][1], 0, h)
        hapi.rotate(0)
        hapi.rect(current_x, y+h-bin_height, 2*space_unit, bin_height)
        hapi.fill(hapi.color['black'])
        hapi.push_matrix()
        hapi.rotate(270)
        hapi.text(d, current_x+space_unit, y+h+5)
        hapi.pop_matrix()
        

        current_x += 3*space_unit


