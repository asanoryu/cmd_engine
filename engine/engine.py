import curses
from dataclasses import dataclass
from .engine_types import Point


class Engine:
    """ The main engine class with functionality to draw things on screen"""

    def __init__(self, filler="#"):
        self._screen = curses.initscr()
        self.max_y, self.max_x = self._screen.getmaxyx()
        self._filler = filler
        self._screen_buffer = [
            [self._filler for i in range(self.max_x)] for j in range(self.max_y)
        ]

    def _reset_buffer(self):
        """ sets the screen buffer to initial value"""
        self._screen_buffer = [
            [self._filler for i in range(self.max_x)] for j in range(self.max_y)
        ]

    def set_pixel(self, pos: Point, val: str = "."):
        """ sets the pixel in pos(x,y) to val """
        if pos.x > self.max_x:
            return
        if pos.y > self.max_y:
            return
        self._screen_buffer[pos.x][pos.y] = val

    def draw_frame(self):
        """ dumps the buffer to screen and draws it"""
        self._screen.clear()
        self._set_frame()
        self._reset_buffer()
        self._screen.refresh()

    def _set_frame(self):
        """ sets the current frame with the content from the _screen_buffer"""
        for y in range(self.max_y):
            for x in range(self.max_x):
                try:
                    self._screen.addstr(y, x, self._screen_buffer[x][y])
                except IndexError:
                    pass

    def _draw_line_low(self, x0: int, y0: int, x1: int, y1: int, symbol:str):
        """ helper for drawing a line with low slope """
        dx = x1 - x0
        dy = y1 - y0
        yi = 1
        if dy < 0:
            yi = -1
            dy = -dy
        D = 2 * dy - dx
        y = y0

        for x in range(x0, x1):
            self.set_pixel(Point(x, y), symbol)
            if D > 0:
                y = y + yi
                D = D - 2 * dx
            D = D + 2 * dy

    def _draw_line_high(self, x0: int, y0: int, x1: int, y1: int, symbol:str):
        """ helper for drawing a line with a high slope """
        dx = x1 - x0
        dy = y1 - y0
        xi = 1
        if dx < 0:
            xi = -1
            dx = -dx
        D = 2 * dx - dy
        x = x0

        for y in range(y0, y1):
            self.set_pixel(Point(x, y), symbol)
            if D > 0:
                x = x + xi
                D = D - 2 * dy
            D = D + 2 * dx

    def draw_line(self, start_pnt: Point, end_pnt: Point, symbol:str ='#'):
        """ draws a line with # from starting point to end_point """
        if abs(end_pnt.y - start_pnt.y) < abs(end_pnt.x - start_pnt.x):
            if start_pnt.x > end_pnt.x:
                self._draw_line_low(end_pnt.x, end_pnt.y, start_pnt.x, start_pnt.y, symbol)
            else:
                self._draw_line_low(start_pnt.x, start_pnt.y, end_pnt.x, end_pnt.y, symbol)
        else:
            if start_pnt.y > end_pnt.y:
                self._draw_line_high(end_pnt.x, end_pnt.y, start_pnt.x, start_pnt.y, symbol)
            else:
                self._draw_line_high(start_pnt.x, start_pnt.y, end_pnt.x, end_pnt.y, symbol)

    def draw_rect(self, top_l: Point, bot_r: Point):
        """ draws an axis aligned rectangle given the top left and bottom right points"""
        top_r = Point(top_l.x, bot_r.y)
        bot_l = Point(bot_r.x, top_l.y)
        self.draw_line(top_l, top_r)
        self.draw_line(top_r, bot_r)
        self.draw_line(top_l, bot_l)
        self.draw_line(bot_l, bot_r)

    def draw_triangle(self, p1: Point, p2: Point, p3: Point):
        """ draws a triangle given 3 points """
        self.draw_line(p1, p2)
        self.draw_line(p1, p3)
        self.draw_line(p2, p3)

    def run(self):
        """
            Get user input
            Update the game state
            Draw the game
            should be overridden
        """
        raise NotImplementedError
