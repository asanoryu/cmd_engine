# cmd_engine
game engine in terminal


Example usage 

    class TestEngine(Engine):
      def __init__(self, filler="#"):
          super().__init__(filler=filler)
          self._start = Point(20, 10)
          self._end = Point(50, 25)
          self._p3 = Point(30, 20)

      def run(self):
          """ override run """
          while True:
              try:
                  self.draw_triangle(self._start, self._end, self._p3)
                  self.draw_frame()

                  time.sleep(0.016)

              except KeyboardInterrupt:
                  sys.exit()


    eng = TestEngine(filler=" ")
    eng.run()
