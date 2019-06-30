import time

from engine.engine import Engine
from engine.engine_types import Point, TIMEOUT_60FPS

class TestEngine(Engine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start = Point(3, 10)
        self.end = Point(10, 30)

    def run(self):
        while True:
            self.draw_line(self.start, self.end)
            self.draw_frame()
            time.sleep(TIMEOUT_60FPS)
            

eng = TestEngine(filler=' ')
eng.run()