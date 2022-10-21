

class RippleGraph:
    def __init__(self, hapi, x, y, size, data: dict, val_range: list):
        self.x = x
        self.y = y
        self.size = size
        self.data = data
        self.val_range = val_range
        self.cols = [] # must be itertools.cycle
        self.hapi = hapi

        # --- have fixed colors for circles ---
        for i in self.data:
            col = next(hapi.candy_colors_list)
            self.cols.append(col)

    def draw(self):
        arc_wid_s = self.size
        arc_wid_x = self.x
        arc_wid_y = self.y

        i = -1
        for key in self.data: # {'x':1}
            i += 1
            d = self.data[key]

            self.hapi.stroke_size(5)

            end_rad = (d / self.val_range) * (self.hapi.PI * 2)

            a_size = arc_wid_s - (i * 30)
            pad = (arc_wid_s - a_size) // 2

            # --- background arc ---
            self.hapi.stroke(self.hapi.colors['candy_gray'])
            self.hapi.arc(
                arc_wid_x + pad,
                arc_wid_y + pad,
                a_size,
                a_size,
                0 + (1.5 * self.hapi.PI),
                self.hapi.PI * 2 + (1.5 * self.hapi.PI),
            )

            # --- colored arc ---
            self.hapi.stroke(self.cols[i])
            self.hapi.arc(
                arc_wid_x + pad,
                arc_wid_y + pad,
                a_size,
                a_size,
                0 + (1.5 * self.hapi.PI),
                end_rad + (1.5 * self.hapi.PI),
            )


class LockButton:
    def __init__(self, x, y, hapi, lock_pattern_obj, num=0):
        self.x = x
        self.y = y
        self.hapi = hapi
        self.num = num
        self.lock_pattern_obj = lock_pattern_obj

    def coords(self):
        return (self.x, self.y)

    def draw(self):
        hapi = self.hapi

        hapi.fill(0)
        hapi.ellipse(self.x, self.y, 20, 20)

    def update(self):
        hapi = self.hapi

        if hapi.pygame.mouse.get_pressed()[0]:

            mouse_coords = (hapi.mouseX(), hapi.mouseY())

            if hapi.dist(self.coords(), mouse_coords) <= 20:

                if self.coords() not in self.lock_pattern_obj.attempt_button_coords:
                    
                    self.lock_pattern_obj.attempt_button_ids.append(self.num)
                    self.lock_pattern_obj.attempt_button_coords.append(self.coords())

    def run(self):
        self.update()
        self.draw()


class LockPattern:
    def __init__(self, hapi, win_pattern, on_win=None, pattern_length=7, row=5, col=5):
        self.attempt_button_coords = [] # coords for lock buttons in user pattern
        self.attempt_button_ids = [] # ids of lock buttons in user pattern
        self.buttons = [] # list of buttons to display
        self.display_win = False
        self.pattern = win_pattern # [1, 2, 3, 4, 5, 6, 7] # ids of password
        self.hapi = hapi
        self.on_win = on_win
        self.pattern_length = pattern_length
        self.row = col # it's good as it is
        self.col = row 


        # --- checks ---

        if not self.pattern_length == len(self.pattern):
            raise Exception('Wining pattern length should be of size as set: {}'.format(self.pattern_length))


        if (self.row * self.col) < len(self.pattern):
            raise Exception('Pattern length cannot be less than row * col')

        # --- reset button ---
        def reset_clicked(this):
            self.attempt_button_coords = []
            self.attempt_button_ids = []
            self.display_win = False


        reset_button_styles = {
            "hover_background_color": (200, 200, 200),
            "font_size": 10,
            "background_color": (210, 210, 210),
            "on_click": reset_clicked,
            "curve": 1,
        }
        self.reset_button = hapi.button(250, 10, 150, 20, "Reset", reset_button_styles)


        # --- initialise buttons ---
        button_id = 1
        for x in range(self.row):
            for y in range(self.col):

                self.buttons.append(LockButton(x * 50 + 10, y * 50 + 10, self.hapi, 
                    self,
                     num=button_id))
                button_id += 1

    def update(self):
        # --- draw lock pattern ---
        hapi = self.hapi 

        hapi.fill(0)
        for i, c in enumerate(self.attempt_button_coords):
            try:
                hapi.stroke_size(5)
                hapi.stroke(hapi.color["green"])
                hapi.line(
                    c[0] + 10,
                    c[1] + 10,
                    self.attempt_button_coords[i + 1][0] + 10,
                    self.attempt_button_coords[i + 1][1] + 10,
                )
            except Exception as e:
                pass

        # --- draw last part of pattern ---
        try:
            hapi.line(
                self.attempt_button_coords[-1][0] + 10,
                self.attempt_button_coords[-1][1] + 10,
                hapi.mouseX(),
                hapi.mouseY(),
            )
        except:
            pass

        # --- display lock buttons ---
        for b in self.buttons:
            b.run()


        # --- if max pattern length ---
        if len(self.attempt_button_coords) >= self.pattern_length:

            if self.attempt_button_ids == self.pattern:
                self.display_win = True

            self.attempt_button_coords = []
            self.attempt_button_ids = []

        # --- right password found ---
        if self.display_win:
            if self.on_win is None:
                self.hapi.fill((200, 200, 50))
                self.hapi.font_size(30)
                self.hapi.text("Right password!", 300, 50)
            else:
                self.on_win()

        # self.reset_button.update()
