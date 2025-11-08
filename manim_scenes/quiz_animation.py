"""
Quiz Animation Scene for Educational Videos
Integrates with the csv-to-video-generator project for creating animated quiz questions
"""

from manim import *


class QuizQuestion(Scene):
    """Animated quiz question scene"""

    def construct(self):
        # Question configuration
        question_text = "What is the capital of France?"
        options = [
            "A) London",
            "B) Paris",
            "C) Berlin",
            "D) Madrid"
        ]
        correct_answer = "B"

        # Create title
        title = Text("Quiz Time!", font_size=56, color=YELLOW)
        title.to_edge(UP, buff=0.5)

        # Create question
        question = Text(question_text, font_size=36, color=WHITE)
        question.next_to(title, DOWN, buff=1)

        # Animate title and question
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeIn(question, shift=DOWN))
        self.wait(1)

        # Create options
        option_group = VGroup()
        for i, option in enumerate(options):
            option_text = Text(option, font_size=28)
            if i > 0:
                option_text.next_to(option_group[-1], DOWN, buff=0.4, aligned_edge=LEFT)
            else:
                option_text.next_to(question, DOWN, buff=1)

            option_group.add(option_text)

        # Animate options one by one
        for option_text in option_group:
            self.play(FadeIn(option_text, shift=RIGHT), run_time=0.5)
            self.wait(0.3)

        self.wait(2)

        # Highlight correct answer
        correct_index = ord(correct_answer) - ord('A')
        correct_rect = SurroundingRectangle(
            option_group[correct_index],
            color=GREEN,
            buff=0.15
        )

        self.play(Create(correct_rect))
        self.play(Flash(option_group[correct_index], color=GREEN, flash_radius=0.5))
        self.wait(2)

        # Fade out
        self.play(FadeOut(VGroup(title, question, option_group, correct_rect)))
        self.wait(0.5)


class MultipleQuizQuestions(Scene):
    """Multiple quiz questions in sequence"""

    def construct(self):
        questions_data = [
            {
                "question": "What is 2 + 2?",
                "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
                "correct": "B"
            },
            {
                "question": "What color is the sky?",
                "options": ["A) Red", "B) Green", "C) Blue", "D) Yellow"],
                "correct": "C"
            }
        ]

        for idx, data in enumerate(questions_data):
            self.show_question(
                question_num=idx + 1,
                question_text=data["question"],
                options=data["options"],
                correct_answer=data["correct"]
            )

    def show_question(self, question_num, question_text, options, correct_answer):
        """Display a single quiz question"""

        # Question number
        q_num = Text(f"Question {question_num}", font_size=48, color=YELLOW)
        q_num.to_edge(UP, buff=0.5)

        # Question
        question = Text(question_text, font_size=32, color=WHITE)
        question.next_to(q_num, DOWN, buff=0.8)

        # Show question
        self.play(Write(q_num))
        self.play(FadeIn(question, shift=DOWN))
        self.wait(1)

        # Create and show options
        option_group = VGroup()
        for i, option in enumerate(options):
            option_text = Text(option, font_size=26)
            if i > 0:
                option_text.next_to(option_group[-1], DOWN, buff=0.3, aligned_edge=LEFT)
            else:
                option_text.next_to(question, DOWN, buff=0.8)
            option_group.add(option_text)

        for option_text in option_group:
            self.play(FadeIn(option_text, shift=RIGHT), run_time=0.4)

        self.wait(2)

        # Show correct answer
        correct_index = ord(correct_answer) - ord('A')
        correct_rect = SurroundingRectangle(
            option_group[correct_index],
            color=GREEN,
            buff=0.15
        )

        self.play(Create(correct_rect))
        self.wait(1.5)

        # Clear screen
        self.play(FadeOut(VGroup(q_num, question, option_group, correct_rect)))
        self.wait(0.5)


class AnimatedChart(Scene):
    """Animated bar chart for quiz results"""

    def construct(self):
        # Title
        title = Text("Quiz Results", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Data
        categories = ["Question 1", "Question 2", "Question 3", "Question 4"]
        values = [85, 92, 78, 95]

        # Create axes
        axes = Axes(
            x_range=[0, len(categories), 1],
            y_range=[0, 100, 10],
            x_length=8,
            y_length=5,
            axis_config={"color": BLUE},
        ).shift(DOWN * 0.5)

        # Y-axis label
        y_label = Text("Score (%)", font_size=24).next_to(axes.y_axis, LEFT)

        self.play(Create(axes), Write(y_label))
        self.wait(0.5)

        # Create bars
        bars = VGroup()
        labels = VGroup()

        for i, (category, value) in enumerate(zip(categories, values)):
            # Bar
            bar = Rectangle(
                height=(value / 100) * axes.y_length,
                width=0.6,
                fill_color=BLUE,
                fill_opacity=0.8,
                stroke_color=WHITE
            )

            x_pos = axes.c2p(i + 0.5, 0)[0]
            y_pos = axes.c2p(0, value / 2)[1]
            bar.move_to([x_pos, y_pos, 0])

            # Label
            label = Text(f"{value}%", font_size=20, color=WHITE)
            label.next_to(bar, UP, buff=0.1)

            # Category label
            cat_label = Text(category, font_size=18, color=WHITE)
            cat_label.next_to(axes.c2p(i + 0.5, 0), DOWN, buff=0.3)

            bars.add(bar)
            labels.add(VGroup(label, cat_label))

        # Animate bars growing
        for bar, label_group in zip(bars, labels):
            self.play(
                GrowFromEdge(bar, DOWN),
                run_time=0.8
            )
            self.play(FadeIn(label_group), run_time=0.3)

        self.wait(2)

        # Average line
        avg_value = sum(values) / len(values)
        avg_line = DashedLine(
            axes.c2p(0, avg_value),
            axes.c2p(len(categories), avg_value),
            color=YELLOW,
            stroke_width=3
        )
        avg_text = Text(f"Average: {avg_value:.1f}%", font_size=24, color=YELLOW)
        avg_text.next_to(avg_line, RIGHT, buff=0.2)

        self.play(Create(avg_line), Write(avg_text))
        self.wait(2)

        # Fade out
        self.play(FadeOut(VGroup(title, axes, y_label, bars, labels, avg_line, avg_text)))
        self.wait(0.5)


class IntroOutro(Scene):
    """Intro/Outro animation for quiz videos"""

    def construct(self):
        # Intro
        title = Text("Educational Quiz", font_size=64, color=YELLOW)
        subtitle = Text("Test Your Knowledge!", font_size=36, color=BLUE)
        subtitle.next_to(title, DOWN, buff=0.5)

        self.play(
            Write(title),
            FadeIn(subtitle, shift=UP),
            run_time=2
        )
        self.wait(1)

        # Animated circle effect
        circle = Circle(radius=4, color=BLUE)
        circle.set_stroke(width=8)

        self.play(
            Create(circle),
            title.animate.scale(0.8),
            subtitle.animate.scale(0.8),
            run_time=1.5
        )
        self.wait(1)

        # Fade to black
        self.play(
            FadeOut(VGroup(title, subtitle, circle)),
            run_time=1.5
        )
        self.wait(0.5)


if __name__ == "__main__":
    """
    Run this script directly to render all quiz animations
    """
    import sys
    import subprocess

    script_file = sys.argv[0]
    scenes = [
        "QuizQuestion",
        "MultipleQuizQuestions",
        "AnimatedChart",
        "IntroOutro"
    ]

    for scene in scenes:
        print(f"\n{'='*50}")
        print(f"Rendering {scene}...")
        print('='*50)

        cmd = ["manim", "render", script_file, scene, "-qh"]
        subprocess.run(cmd)

    print("\n✓ All quiz scenes rendered successfully!")
