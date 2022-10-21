scatter plot

![](https://github.com/Abdur-rahmaanJ/hooman/raw/master/assets/scatter_chart.png)


```python
# https://seaborn.pydata.org/examples/different_scatter_variables.html

from hooman import Hooman
import pandas as pd
import os

window_width, window_height = 650, 600
hapi = Hooman(window_width, window_height)


base_path = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(base_path, "data", "diamonds.csv"))

data = {k:list(df[k]) for k in df.columns.values.tolist()}

hapi.background(255)

colx = 'carat'
coly = 'price'

clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
hapi.scatterchart(
        40,
        30,
        500,
        500,
        {
        "data": data,
            "ticks_y": 8,
            "ticks_x": 5,
            "mouse_line": False,
            "range_y": [min(data[coly]), max(data[coly])],
            "range_x": [min(data[colx]), max(data[colx])],
            "show_axes": True,
            "tick_size": 10,
            "show_ticks_x": True,
            "show_ticks_y": True,
            "x": colx,
            "y": coly,
            "hue": "clarity",
            "hue_order": clarity_ranking,
            "size": "depth",
            "plot_background": False,
            "plot_background_grid": True,
            "plot_background_color": (234,234,242),
            "plot_background_grid_color": 200,
            "line_color": 200
        },
    )

while hapi.is_running:
    bg_col = (255, 255, 255)

    hapi.flip_display()
    hapi.event_loop()
```