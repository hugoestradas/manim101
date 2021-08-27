from manim import *

class TracedPathExample(Scene):
    def construct(self):
        # Create circle and dot
        circ = Circle(color=BLUE).shift(4*LEFT)
        dot = Dot(color=BLUE).move_to(circ.get_start())

        # Group dot and circle
        rolling_circle = VGroup(circ, dot)
        trace = TracedPath(circ.get_start)

        rolling_circle.add_updater(lambda m: m.rotate(-0.3))  # Rotate the circle

        self.add(trace, rolling_circle) # add trace and rolling circle to the scene

        # Shift the circle to 8*RIGHT
        self.play(rolling_circle.animate.shift(8*RIGHT), run_time=4, rate_func=linear)
        
