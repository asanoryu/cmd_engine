import time

from engine import Engine, Point


buffer = [
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", "#", "#", "#"],
    [".", ".", "#", "#", "#", "#"],
    [".", "#", "#", "#", "#", "#"],
    [".", "#", "#", "#", "#", "#"],
    [".", "#", "#", "#", "#", "#"],
]


eng = Engine()
# eng.set_screen()
print(f"{eng.max_x} {eng.max_y}")
st = Point(0, 0)
end = Point(30, 30)
eng.draw_line(st, end)

eng.draw_line(Point(0, 30), Point(35, 0))
eng.draw_frame()
time.sleep(4)
