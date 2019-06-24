import curses
import math
import array


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Engine:
    def __init__(self):
        self._screen = curses.initscr()
        # curses.resize_term(250, 100)
        self.max_y, self.max_x = self._screen.getmaxyx()
        self._screen_buffer = [
            ["." for i in range(self.max_x)] for j in range(self.max_y)
        ]

    def _reset_buffer(self):
        self._screen_buffer = [
            ["." for i in range(self.max_x)] for j in range(self.max_y)
        ]

    def set_pixel(self, pos, val="#"):
        if pos.x > self.max_x:
            return
        if pos.y > self.max_y:
            return
        self._screen_buffer[pos.x][pos.y] = val

    def draw_frame(self):
        self._screen.clear()
        self.set_frame()
        self._reset_buffer()
        self._screen.refresh()

    def set_frame(self):
        for y in range(self.max_x - 1):
            for x in range(self.max_y - 1):
                try:
                    self._screen.addstr(y, x, self._screen_buffer[x][y])
                except IndexError:
                    pass

    def _write_debug(self, msg):
        self._screen.addstr(0, 0, msg)

    def _draw_line_low(self, x0, y0, x1, y1):
        dx = x1 - x0
        dy = y1 - y0
        yi = 1
        if dy < 0:
            yi = -1
            dy = -dy
        D = 2 * dy - dx
        y = y0

        for x in range(x0, x1):
            self.set_pixel(Point(x, y))
            if D > 0:
                y = y + yi
                D = D - 2 * dx
            D = D + 2 * dy

    def _draw_line_high(self, x0, y0, x1, y1):
        dx = x1 - x0
        dy = y1 - y0
        xi = 1
        if dx < 0:
            xi = -1
            dx = -dx
        D = 2 * dx - dy
        x = x0

        for y in range(y0, y1):
            self.set_pixel(Point(x, y))
            if D > 0:
                x = x + xi
                D = D - 2 * dy
            D = D + 2 * dx

    def draw_line(self, start_pnt, end_pnt):

        if abs(end_pnt.y - start_pnt.y) < abs(end_pnt.x - start_pnt.x):
            if start_pnt.x > end_pnt.x:
                self._draw_line_low(end_pnt.x, end_pnt.y, start_pnt.x, start_pnt.y)
            else:
                self._draw_line_low(start_pnt.x, start_pnt.y, end_pnt.x, end_pnt.y)
        else:
            if start_pnt.y > end_pnt.y:
                self._draw_line_high(end_pnt.x, end_pnt.y, start_pnt.x, start_pnt.y)
            else:
                self._draw_line_high(start_pnt.x, start_pnt.y, end_pnt.x, end_pnt.y)

