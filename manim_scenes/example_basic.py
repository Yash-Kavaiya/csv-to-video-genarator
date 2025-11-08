"""
Example Basic Manim Scene
This file demonstrates a simple Manim animation that will be automatically rendered when pushed.
"""

from manim import *


class BasicShapes(Scene):
    """Basic shapes animation example"""

    def construct(self):
        # Title
        title = Text("Welcome to Automated Manim!", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create shapes
        circle = Circle(radius=1, color=BLUE)
        square = Square(side_length=2, color=RED)
        triangle = Triangle(color=GREEN)

        # Arrange shapes
        shapes = VGroup(circle, square, triangle).arrange(RIGHT, buff=1)

        # Animate shapes
        self.play(Create(circle))
        self.play(Create(square))
        self.play(Create(triangle))
        self.wait(1)

        # Transform
        self.play(
            circle.animate.shift(UP),
            square.animate.rotate(PI/4),
            triangle.animate.shift(DOWN)
        )
        self.wait(1)

        # Color change
        self.play(
            circle.animate.set_color(YELLOW),
            square.animate.set_color(PURPLE),
            triangle.animate.set_color(ORANGE)
        )
        self.wait(1)

        # Fade out
        self.play(FadeOut(VGroup(title, circle, square, triangle)))
        self.wait(0.5)


class MathEquation(Scene):
    """Mathematical equation animation"""

    def construct(self):
        # Create equation
        equation = MathTex(
            r"e^{i\pi} + 1 = 0",
            font_size=72
        )

        # Animate equation
        self.play(Write(equation))
        self.wait(2)

        # Transform to components
        components = VGroup(
            MathTex(r"e^{i\pi}", color=BLUE),
            MathTex(r"+", color=WHITE),
            MathTex(r"1", color=RED),
            MathTex(r"=", color=WHITE),
            MathTex(r"0", color=GREEN)
        ).arrange(RIGHT, buff=0.3)

        self.play(TransformMatchingTex(equation, components))
        self.wait(2)

        # Highlight each component
        for comp in components:
            self.play(Indicate(comp, scale_factor=1.5))
            self.wait(0.5)

        self.wait(1)
        self.play(FadeOut(components))


class DataVisualization(Scene):
    """Simple data visualization example"""

    def construct(self):
        # Title
        title = Text("Data Visualization", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 100, 10],
            x_length=7,
            y_length=5,
            axis_config={"color": BLUE},
        )

        # Add labels
        labels = axes.get_axis_labels(x_label="Time", y_label="Value")

        # Create graph
        graph = axes.plot(lambda x: x**2, color=YELLOW)

        # Animate
        self.play(Create(axes), Write(labels))
        self.wait(1)
        self.play(Create(graph), run_time=3)
        self.wait(2)

        # Add point
        dot = Dot(axes.c2p(5, 25), color=RED)
        label = Text("(5, 25)", font_size=24).next_to(dot, UP)

        self.play(FadeIn(dot), Write(label))
        self.wait(2)

        # Fade out
        self.play(FadeOut(VGroup(title, axes, labels, graph, dot, label)))
        self.wait(0.5)


if __name__ == "__main__":
    """
    This allows running the script directly with:
    python manim_scenes/example_basic.py

    Or using manim command:
    manim render manim_scenes/example_basic.py BasicShapes -ql
    """
    import sys
    import subprocess

    # Get the script filename
    script_file = sys.argv[0]

    # Default to rendering all scenes at high quality
    scenes = ["BasicShapes", "MathEquation", "DataVisualization"]

    for scene in scenes:
        print(f"\n{'='*50}")
        print(f"Rendering {scene}...")
        print('='*50)

        cmd = ["manim", "render", script_file, scene, "-qh"]
        subprocess.run(cmd)

    print("\n✓ All scenes rendered successfully!")
