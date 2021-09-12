%%manim -qm -v WARNING FunctionExample
import numpy as np

class FunctionExample(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5, .5],
            y_range=[-3, 4, 1],
            x_axis_config={"numbers_to_include": [-4, -3, 3, 4]},
            y_axis_config={"numbers_to_include": [-2, 2, 3]},
            tips=True
        )
        axes_labels=axes.get_axis_labels()
        # Get the graph of a simple functions
        graph = axes.get_graph(lambda x: np.sin(1/x), color=RED)
        # Set up its label
        graph_label = axes.get_graph_label(
            graph, x_val=1, direction=2 * UP + RIGHT,
           label=r'f(x) = \sin(\frac{1}{x})', color=DARK_BLUE
        )

        # Graph the axes components together
        axes_group = VGroup(axes, axes_labels)
        
        # Animate
        self.play(Create(axes_group), run_time=2)
        self.wait(0.25)
        self.play(Create(graph), run_time=3)
        self.play(Write(graph_label), run_time=2)
