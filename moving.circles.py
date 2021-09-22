from manim import *

class GroupCircles(Scene):
    def construct(self):
        # Create circles
        circle_green = Circle(color=GREEN)
        circle_blue = Circle(color=BLUE)
        circle_red = Circle(color=RED)

        # Set initial positions
        circle_green.shift(LEFT)
        circle_blue.shift(RIGHT)

        # Create 2 different groups
        gr = VGroup(circle_green, circle_red)
        gr2 = VGroup(circle_blue)
        self.add(gr, gr2)  # add two groups to the scene
        self.wait()

        self.play((gr + gr2).animate.shift(DOWN))  # shift 2 groups down

        self.play(gr.animate.shift(RIGHT))  # move only 1 group
        self.play(gr.animate.shift(UP))

        self.play((gr + gr2).animate.shift(RIGHT))  # shift 2 groups to the right
        self.play(circle_red.animate.shift(RIGHT))
        self.wait()
