import copy

from .check import check_params


def barchart(hapi, x, y, w, h, params):
    options = {
        "ticks_y": 10,
        "tick_size": 5,
        "range_y": [0, 100],
        "data": {"a": 10, "b": 20},
        "bin_color": (255, 99, 97),
        "line_color": (200, 200, 200),
        "text_color": (100, 100, 100),
        "mouse_line": False,
    }
    check_params(params, options, "bar chart")
    options.update(params)
    hapi.stroke_size(2)
    hapi.stroke(options["line_color"])
    hapi.line(x, y, x, y + h)
    hapi.line(x, y + h, x + w, y + h)
    hapi.fill(options["text_color"])
    y_top_val = options["range_y"][1]
    for t in range(options["ticks_y"]):
        hapi.line(
            x,
            y + (t * (h // options["ticks_y"])),
            x - options["tick_size"],
            y + (t * (h // options["ticks_y"])),
        )
        hapi.text(y_top_val, x - 20, y + (t * (h // options["ticks_y"])) - 10)
        y_top_val -= (options["range_y"][1] - options["range_y"][0]) // options[
            "ticks_y"
        ]

    num_data = len(options["data"].keys())
    divs = 1 + 1 + (num_data * 2) + (num_data - 1)
    space_unit = w // divs
    current_x = x + space_unit
    for i, d in enumerate(options["data"]):
        hapi.fill(options["bin_color"])
        bin_height = hapi.constrain(
            options["data"][d], options["range_y"][0], options["range_y"][1], 0, h
        )
        hapi.rotate(0)
        hapi.rect(current_x, y + h - bin_height, 2 * space_unit, bin_height)
        hapi.fill(hapi.color["black"])
        hapi.push_matrix()
        hapi.rotate(270)
        hapi.text(d, current_x + space_unit, y + h + 5)
        hapi.pop_matrix()
        current_x += 3 * space_unit

    if options["mouse_line"]:
        hapi.stroke_size(2)
        hapi.stroke(hapi.color["red"])
        l_height = hapi.mouseY()
        if hapi.mouseY() < y:
            l_height = y
        elif hapi.mouseY() > y + h:
            l_height = y + h
        hapi.line(x, l_height, x + w, l_height)


def linechart(hapi, x, y, w, h, params):
    options = {
        "ticks_y": 10,
        "ticks_x": 10,
        "tick_size": 5,
        "range_y": [0, 100],
        "range_x": [0, 100],
        "lines": [
            {
                "label": "---",
                "color": (255, 0, 0),
                "data": [[1, 1]],
                "values_window": 200,
            }
        ],
        "labels": ["apple", "", "", "tree"],
        "line_color": (200, 200, 200),
        "text_color": (100, 100, 100),
        "mouse_line": False,
        "mouse_line_color": (255, 0, 0),
        "graph_color": (0, 0, 0),
        "show_axes": True,
        "show_ticks_x": True,
        "show_ticks_y": True,
        "x_axis_label": "x_axis_label",
        "y_axis_label": "y_axis_label",
        "plot_background": True,
        "plot_grid": True,
        "plot_background_color": (234, 234, 242),
        "plot_grid_color": 255,
    }
    check_params(params, options, "line chart")
    options.update(params)
    hapi.stroke_size(2)

    # --- plot background ---

    if options["plot_background"]:

        hapi.fill(options["plot_background_color"])
        hapi.rect(x, y, w, h)

    # --- plot background grid ---

    if options["plot_grid"]:

        hapi.stroke(options["plot_grid_color"])

        # --- vertical
        bg_grid_x1 = x
        bg_grid_y1 = y
        bg_grid_x2 = x
        bg_grid_y2 = y + h
        line_num = 1
        while bg_grid_x1 <= x + w:
            if 1 < line_num < options["ticks_x"] + 1:
                hapi.line(bg_grid_x1, bg_grid_y1, bg_grid_x2, bg_grid_y2)
            bg_grid_x1 += w // options["ticks_x"]
            bg_grid_x2 += w // options["ticks_x"]
            line_num += 1

        # --- horizontal
        bg_grid_x1 = x
        bg_grid_y1 = y
        bg_grid_x2 = x + w
        bg_grid_y2 = y
        line_num = 1
        while bg_grid_y1 <= y + h:
            if 1 < line_num < options["ticks_y"] + 1:
                hapi.line(bg_grid_x1, bg_grid_y1, bg_grid_x2, bg_grid_y2)
            bg_grid_y1 += h // options["ticks_y"]
            bg_grid_y2 += h // options["ticks_y"]
            line_num += 1

    # --- axes ---

    if options["show_axes"]:
        hapi.stroke(options["line_color"])
        hapi.line(x, y, x, y + h)
        hapi.line(x, y + h, x + w, y + h)

    hapi.fill(options["text_color"])

    # --- axes labels

    hapi.push_matrix()
    hapi.rotate(90)
    hapi.text(
        options["x_axis_label"],
        x - 35,
        y + (h - (hapi._font.size(options["x_axis_label"])[0]) // 2),
    )
    hapi.pop_matrix()

    hapi.text(
        options["y_axis_label"],
        x + (w - (hapi._font.size(options["y_axis_label"])[0]) // 2),
        y + h + 35,
    )

    y_top_val = options["range_y"][1]
    for t in range(options["ticks_y"]):
        if options["show_ticks_y"]:
            hapi.line(
                x,
                y + (t * (h // options["ticks_y"])),
                x - options["tick_size"],
                y + (t * (h // options["ticks_y"])),
            )
        hapi.text(y_top_val, x - 20, y + (t * (h // options["ticks_y"])) - 10)
        y_top_val -= (options["range_y"][1] - options["range_y"][0]) // options[
            "ticks_y"
        ]

    x_val = options["range_x"][0]
    for t in range(options["ticks_x"] + 1):
        if options["show_ticks_x"]:
            hapi.line(
                x + (t * (w // options["ticks_x"])),
                y + h,
                x + (t * (w // options["ticks_x"])),
                y + h + options["tick_size"],
            )
        hapi.push_matrix()
        hapi.rotate(270)
        hapi.text(x_val, x + (t * (w // options["ticks_x"])), y + h + 5)
        hapi.pop_matrix()
        x_val += (options["range_x"][1] - options["range_x"][0]) // options["ticks_x"]

    for l_index, line in enumerate(copy.deepcopy(options["lines"])):
        for i, d in enumerate(copy.deepcopy(line["data"])):

            try:
                x1 = hapi.constrain(
                    d[0], options["range_x"][0], options["range_x"][1], x, x + w
                )
                y1 = (
                    y
                    + h
                    - hapi.constrain(
                        d[1], options["range_y"][0], options["range_y"][1], y, y + h
                    )
                    + y
                )

                x2 = hapi.constrain(
                    line["data"][i + 1][0],
                    options["range_x"][0],
                    options["range_x"][1],
                    x,
                    x + w,
                )
                y2 = (
                    y
                    + h
                    - hapi.constrain(
                        line["data"][i + 1][1],
                        options["range_y"][0],
                        options["range_y"][1],
                        y,
                        y + h,
                    )
                    + y
                )

                # 60 is arbitrary value
                # hapi.fill(hapi.color['yellow'])
                # print(x1, y1)
                hapi.stroke_size(2)
                hapi.stroke(line["color"])
                hapi.line(x1, y1, x2, y2)
                # hapi.line(x1, y1, x2, y2)
            except IndexError:
                pass

            # if len(line["data"]) > line["values_window"]:
            # # options["lines"][l_index]["data"].pop(0)

            #     del options["lines"][l_index]['data'][0]

    if options["mouse_line"]:
        hapi.stroke_size(2)
        hapi.stroke(options["mouse_line_color"])
        limit_y = hapi.mouseY()
        limit_x = hapi.mouseX()
        if limit_y < y:
            limit_y = y
        elif limit_y > y + h:
            limit_y = y + h
        if limit_x < x:
            limit_x = x
        elif limit_x > x + w:
            limit_x = x + w

        hapi.line(x, limit_y, x + w, limit_y)
        hapi.line(limit_x, y, limit_x, y + h)
        # tex = "{} {}".format(limit_x, limit_y)
        # hapi.text(tex, 100, 100)

    # legend

    legend_x_start = x + w + 10
    legend_y_start = y
    legend_y = legend_y_start

    for line in options["lines"]:
        hapi.fill(line["color"])
        hapi.ellipse(legend_x_start, legend_y, 10, 10)
        hapi.font_size(15)
        hapi.text(line["label"], legend_x_start + 15, legend_y)
        legend_y += 10


def piechart(hapi, x, y, radius, data, start_rad=0):
    first_run = True
    total = 0
    if first_run:
        for d in data:
            total += d[1]
        first_run = False

    previous_a = 0
    for i, d in enumerate(data):
        hapi.fill(d[2])
        end_a = previous_a + (d[1] / total) * 360
        hapi.fill_arc(x, y, radius, previous_a, end_a, start_rad=start_rad)
        previous_a = end_a


def scatterchart(hapi, x, y, w, h, params):
    options = {
        "ticks_y": 10,
        "ticks_x": 10,
        "tick_size": 5,
        "range_y": [0, 100],
        "range_x": [0, 100],
        "data": {
            "carat": [0.23, 0.21, 0.23, 0.29, 0.31, 0.24, 0.24, 0.26, 0.22, 0.23],
            "cut": [
                "Ideal",
                "Premium",
                "Good",
                "Premium",
                "Good",
                "Very Good",
                "Very Good",
                "Very Good",
                "Fair",
            ],
            "color": ["E", "E", "E", "I", "J", "J", "I", "H", "E", "H"],
            "clarity": [
                "SI2",
                "SI1",
                "VS1",
                "VS2",
                "SI2",
                "VVS2",
                "VVS1",
                "SI1",
                "VS2",
                "VS1",
            ],
            "depth": [61.5, 59.8, 56.9, 62.4, 63.3, 62.8, 62.3, 61.9, 65.1, 59.4],
            "table": [55, 61, 65, 58, 58, 57, 57, 55, 61, 61],
            "price": [326, 326, 327, 334, 335, 336, 336, 337, 337, 338],
            "x": [3.95, 3.89, 4.05, 4.2, 4.34, 3.94, 3.95, 4.07, 3.87, 4],
            "y": [3.98, 3.84, 4.07, 4.23, 4.35, 3.96, 3.98, 4.11, 3.78, 4.05],
            "z": [2.43, 2.31, 2.31, 2.63, 2.75, 2.48, 2.47, 2.53, 2.49, 2.39],
        },
        "hue": None,
        "hue_order": [],
        "size": None,
        "text_color": (100, 100, 100),
        "mouse_line": False,
        "mouse_line_color": (255, 0, 0),
        "graph_color": (0, 0, 0),
        "show_axes": True,
        "show_ticks_x": True,
        "show_ticks_y": True,
        "x": "price",
        "y": "carat",
        "plot_background": True,
        "plot_grid": True,
        "plot_background_color": (234, 234, 242),
        "plot_grid_color": 255,
        "line_color": 200,
        "strong_color": (107, 107, 255),
        "light_color": (235, 235, 255),
        "type": "normal",
        "kind": "rect",
        "hist_color": "b",
        "hist_color_invert": False,
    }

    check_params(params, options, "scatter chart")
    options.update(params)

    hapi.stroke_size(2)
    hapi.font_size(15)

    # --- plot background ---

    if options["plot_background"]:

        hapi.fill(options["plot_background_color"])
        hapi.rect(x, y, w, h)

    # --- mouse line ---

    if options["mouse_line"]:
        hapi.stroke_size(2)
        hapi.stroke(options["mouse_line_color"])
        limit_y = hapi.mouseY()
        limit_x = hapi.mouseX()
        if limit_y < y:
            limit_y = y
        elif limit_y > y + h:
            limit_y = y + h
        if limit_x < x:
            limit_x = x
        elif limit_x > x + w:
            limit_x = x + w

        hapi.line(x, limit_y, x + w, limit_y)
        hapi.line(limit_x, y, limit_x, y + h)

    # --- scatter ---

    xvals = options["data"][options["x"]]
    yvals = options["data"][options["y"]]
    # print(xvals[:10], yvals[:10])
    # hapi.set_alpha(100)

    if options["hue"]:
        strong_blue = options["strong_color"]
        light_blue = options["light_color"]
        strong_blue_hls = hapi.rgb_to_hls(*strong_blue)
        light_blue_hls = hapi.rgb_to_hls(*light_blue)
        l_strong = strong_blue_hls[1]
        l_light = light_blue_hls[1]

        delta_l = l_strong - l_light
        steps = len(options["hue_order"])
        delta_change = delta_l / steps

        c_map = {}

        color_l = l_strong

        legend_y = y + 10
        hapi.fill(0)
        hapi.text(options["hue"], x + w + 10, y)
        for c in options["hue_order"]:
            color_hue = hapi.hls_to_rgb(strong_blue_hls[0], color_l, strong_blue_hls[2])
            c_map[c] = color_hue
            color_l += delta_change

            # --- legend

            # --- --- hue

            hapi.fill(color_hue)
            hapi.ellipse(x + w + 10, legend_y, 10, 10)
            hapi.text(c, x + w + 10 + 15, legend_y)
            legend_y += 10

    hue = options["hue"]

    # --- --- size

    if options["size"]:
        min_size = min(options["data"][options["size"]])
        max_size = max(options["data"][options["size"]])

        hapi.fill(0)
        legend_y += 10
        hapi.text(options["size"], x + w + 10, legend_y)
        legend_y += 10

        d_size = (max_size - min_size) / 5
        start_size = min_size
        ellipse_size = 0
        for i in range(5):
            ellipse_size = i + 1
            hapi.ellipse(x + w + 10, legend_y, ellipse_size, ellipse_size)
            hapi.text(round(start_size, 2), x + w + 15, legend_y)
            start_size += d_size
            legend_y += 10

        ellipse_size += 1
        hapi.ellipse(x + w + 10, legend_y, ellipse_size, ellipse_size)
        hapi.text(round(start_size, 2), x + w + 15, legend_y)

    # /--- legend

    # --- actual plotting

    if options["type"] == "normal":
        for i, vx in enumerate(xvals):
            if options["hue"]:
                current_hue = options["data"][options["hue"]][i]
                current_color = c_map[current_hue]
            else:
                current_color = options["graph_color"]

            hapi.fill(current_color)

            ex = hapi.constrain(
                vx,
                options["range_x"][0],
                options["range_x"][1],
                x,
                x + w,
            )
            ey = (
                y
                + h
                - hapi.constrain(
                    yvals[i],
                    options["range_y"][0],
                    options["range_y"][1],
                    y,
                    y + h,
                )
                + y
            )

            if options["size"]:
                size = options["data"][options["size"]][i]
                ellipse_size = (size / max_size) * 5
            else:
                ellipse_size = 5
            hapi.ellipse(ex, ey, ellipse_size, ellipse_size)
    elif options["type"] == "hist":

        range_x = (
            max(options["data"][options["x"]]) - min(options["data"][options["x"]])
        ) // options["ticks_x"]
        range_y = (
            max(options["data"][options["y"]]) - min(options["data"][options["y"]])
        ) // options["ticks_y"]

        m = {}

        # for xi in range(options['ticks_x']+1):
        #     for yi in range(options['ticks_y']+1):
        #         m[str(xi*range_x)+'-'+str(yi*range_y)] = 0

        total = 0
        for x_point, y_point in zip(
            options["data"][options["x"]], options["data"][options["y"]]
        ):
            xi = x_point / (
                (options["range_x"][1] - options["range_x"][0]) / options["ticks_x"]
            )
            yi = y_point / (
                (options["range_y"][1] - options["range_y"][0]) / options["ticks_y"]
            )

            yi = options["ticks_y"] - yi

            xi = int(xi)
            yi = int(yi)

            if (xi, yi) not in m:
                m[(xi, yi)] = 1
                total += 1
            else:
                m[(xi, yi)] += 1
                total += 1

        li = [[k, m[k]] for k in m]

        sorted_li = sorted(li, key=lambda l: l[1], reverse=True)

        rect_w = w // options["ticks_x"]
        rect_h = h // options["ticks_y"]

        max_key = max(m, key=m.get)
        max_val = m[max_key]
        for xi in range(options["ticks_x"]):
            for yi in range(options["ticks_y"]):
                if (xi, yi) in m:

                    if options["hist_color_invert"]:
                        col = (m[(xi, yi)] / max_val) * 255
                    else:
                        col = (((max_val - m[(xi, yi)]) / max_val)) * 255

                    check("scatterchart", "hist_color", options["hist_color"])
                    if options["hist_color"] == "r":
                        col_rect = (int(col), 0, 0)
                    if options["hist_color"] == "g":
                        col_rect = (0, int(col), 0)
                    if options["hist_color"] == "b":
                        col_rect = (0, 0, int(col))
                    hapi.fill(col_rect)
                else:
                    hapi.fill(255)

                if options["kind"] == "rect":
                    hapi.rect(x + xi * rect_w, y + yi * rect_h, rect_w, rect_h)
                if options["kind"] == "round":
                    hapi.ellipse(x + xi * rect_w, y + yi * rect_h, rect_w, rect_h)
                elif options["kind"] == "hex":
                    err = 1.8 * rect_w
                    if yi % 2 == 0:
                        hapi.regular_polygon(
                            x + xi * rect_w, y + yi * rect_h, rect_w - err, rect_h, 6
                        )
                    else:
                        hapi.regular_polygon(
                            x + xi * rect_w + (err // 4),
                            y + yi * rect_h,
                            rect_w - err,
                            rect_h,
                            6,
                        )

    # --- plot grid ---

    hapi.stroke_size(1)
    if options["plot_grid"]:

        hapi.stroke(options["plot_grid_color"])

        # --- vertical
        bg_grid_x1 = x
        bg_grid_y1 = y
        bg_grid_x2 = x
        bg_grid_y2 = y + h
        line_num = 1
        while bg_grid_x1 <= x + w:
            if 1 < line_num < options["ticks_x"] + 1:
                hapi.line(bg_grid_x1, bg_grid_y1, bg_grid_x2, bg_grid_y2)
            bg_grid_x1 += w // options["ticks_x"]
            bg_grid_x2 += w // options["ticks_x"]
            line_num += 1

        # --- horizontal
        bg_grid_x1 = x
        bg_grid_y1 = y
        bg_grid_x2 = x + w
        bg_grid_y2 = y
        line_num = 1
        while bg_grid_y1 <= y + h:
            if 1 < line_num < options["ticks_y"] + 1:
                hapi.line(bg_grid_x1, bg_grid_y1, bg_grid_x2, bg_grid_y2)
            bg_grid_y1 += h // options["ticks_y"]
            bg_grid_y2 += h // options["ticks_y"]
            line_num += 1

    # --- axes ---

    if options["show_axes"]:
        hapi.stroke(options["line_color"])
        hapi.line(x, y, x, y + h)
        hapi.line(x, y + h, x + w, y + h)

    hapi.fill(options["text_color"])

    # --- axes labels

    hapi.push_matrix()
    hapi.rotate(90)
    hapi.text(options["y"], x - 35, y + (h - (hapi._font.size(options["y"])[0]) // 2))
    hapi.pop_matrix()

    hapi.text(
        options["x"], x + (w - (hapi._font.size(options["x"])[0]) // 2), y + h + 35
    )

    # --- axes

    y_top_val = options["range_y"][1]
    for t in range(options["ticks_y"]):
        if options["show_ticks_y"]:
            hapi.line(
                x,
                y + (t * (h // options["ticks_y"])),
                x - options["tick_size"],
                y + (t * (h // options["ticks_y"])),
            )
        hapi.text(y_top_val, x - 20, y + (t * (h // options["ticks_y"])) - 10)
        y_top_val -= (options["range_y"][1] - options["range_y"][0]) // options[
            "ticks_y"
        ]

    x_val = options["range_x"][0]
    for t in range(options["ticks_x"] + 1):
        if options["show_ticks_x"]:
            hapi.line(
                x + (t * (w // options["ticks_x"])),
                y + h,
                x + (t * (w // options["ticks_x"])),
                y + h + options["tick_size"],
            )
        hapi.push_matrix()
        hapi.rotate(270)
        hapi.text(round(x_val, 2), x + (t * (w // options["ticks_x"])), y + h + 5)
        hapi.pop_matrix()
        x_val += (options["range_x"][1] - options["range_x"][0]) / options["ticks_x"]

        # print(x_val, ((options["range_x"][1] - options["range_x"][0]) / options["ticks_x"]))
