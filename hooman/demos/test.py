# https://github.com/mwaskom/seaborn-data/blob/master/penguins.csv

from hooman import Hooman
import pandas as pd
import os

window_width, window_height = 650, 600
hapi = Hooman(window_width, window_height, svg=True)


base_path = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(base_path, "data", "penguins.csv"))
df = df.fillna(0)

data = {k:list(df[k]) for k in df.columns.values.tolist()}

hapi.background(255)

colx = "bill_length_mm"
coly = "bill_depth_mm"

hapi.scatterchart(
        40,
        30,
        500,
        500,
        {
        "data": data,
            "ticks_y": 12,
            "ticks_x": 12,
            "range_y": [min(data[coly]), max(data[coly])],
            "range_x": [min(data[colx]), max(data[colx])],
            "show_axes": True,
            "tick_size": 10,
            "show_ticks_x": True,
            "show_ticks_y": True,
            "x": colx,
            "y": coly,
            "plot_background": False,
            "plot_grid": False,
            "line_color": 200,
            "type": "hist",
            "hist_color": "g"
        },
    )

hapi.save_svg(os.path.join(base_path, 'file.svg'))
