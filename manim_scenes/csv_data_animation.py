"""
CSV Data Animation Scene
Demonstrates how to create Manim animations from CSV data
Compatible with the csv-to-video-generator project
"""

from manim import *
import csv
import json
from pathlib import Path


class CSVDataVisualization(Scene):
    """Visualize data from CSV files"""

    def construct(self):
        # Sample data (in production, this would come from CSV)
        data = [
            {"name": "Product A", "value": 45},
            {"name": "Product B", "value": 78},
            {"name": "Product C", "value": 62},
            {"name": "Product D", "value": 91},
        ]

        # Title
        title = Text("CSV Data Visualization", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create animated bar chart
        self.create_bar_chart(data, title)

        self.wait(1)
        self.play(FadeOut(*self.mobjects))

    def create_bar_chart(self, data, title):
        """Create an animated bar chart from data"""

        max_value = max(item["value"] for item in data)

        # Create bars
        bars = VGroup()
        labels = VGroup()

        for i, item in enumerate(data):
            # Calculate bar height proportional to value
            bar_height = (item["value"] / max_value) * 4

            bar = Rectangle(
                height=bar_height,
                width=1.2,
                fill_color=interpolate_color(BLUE, RED, item["value"] / max_value),
                fill_opacity=0.8,
                stroke_color=WHITE,
                stroke_width=2
            )

            # Position bars
            x_pos = -4 + i * 2.5
            bar.move_to([x_pos, bar_height / 2 - 2, 0])

            # Value label
            value_label = Text(str(item["value"]), font_size=24, color=WHITE)
            value_label.next_to(bar, UP, buff=0.1)

            # Name label
            name_label = Text(item["name"], font_size=20, color=WHITE)
            name_label.next_to(bar, DOWN, buff=0.3)

            bars.add(bar)
            labels.add(VGroup(value_label, name_label))

            # Animate
            self.play(GrowFromEdge(bar, DOWN), run_time=0.8)
            self.play(FadeIn(value_label), FadeIn(name_label), run_time=0.3)

        self.wait(2)


class DynamicTextAnimation(Scene):
    """Create animated text from CSV questions/answers"""

    def construct(self):
        # Sample Q&A data (would come from CSV in production)
        qa_data = [
            {
                "question": "What is Python?",
                "answer": "A high-level programming language"
            },
            {
                "question": "What is Manim?",
                "answer": "A mathematical animation engine"
            }
        ]

        for qa in qa_data:
            self.show_qa(qa["question"], qa["answer"])

    def show_qa(self, question_text, answer_text):
        """Display question and answer with animation"""

        # Question
        question = Text("Q:", font_size=36, color=YELLOW)
        question.to_edge(LEFT, buff=1).shift(UP * 2)

        q_text = Text(question_text, font_size=32, color=WHITE)
        q_text.next_to(question, RIGHT, buff=0.3)

        # Animate question
        self.play(Write(question))
        self.play(FadeIn(q_text, shift=RIGHT))
        self.wait(1.5)

        # Answer
        answer = Text("A:", font_size=36, color=GREEN)
        answer.next_to(question, DOWN, buff=1, aligned_edge=LEFT)

        a_text = Text(answer_text, font_size=28, color=WHITE)
        a_text.next_to(answer, RIGHT, buff=0.3)

        # Animate answer with typewriter effect
        self.play(Write(answer))
        self.play(AddTextLetterByLetter(a_text), run_time=len(answer_text) * 0.05)
        self.wait(2)

        # Clear
        self.play(FadeOut(VGroup(question, q_text, answer, a_text)))
        self.wait(0.5)


class NumberAnimation(Scene):
    """Animate numbers and statistics from CSV data"""

    def construct(self):
        # Sample statistics
        stats = [
            {"label": "Total Users", "value": 1234},
            {"label": "Active Today", "value": 567},
            {"label": "New Signups", "value": 89},
        ]

        # Title
        title = Text("Statistics Dashboard", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Create stat displays
        stat_group = VGroup()

        for i, stat in enumerate(stats):
            # Container
            container = VGroup()

            # Number (animated counter)
            number = Integer(0, font_size=56, color=GREEN)

            # Label
            label = Text(stat["label"], font_size=24, color=WHITE)
            label.next_to(number, DOWN, buff=0.3)

            container.add(number, label)

            if i == 0:
                container.move_to(UP * 0.5)
            else:
                container.next_to(stat_group[-1], DOWN, buff=1)

            stat_group.add(container)

            # Animate appearance
            self.play(FadeIn(label))

            # Animate counter
            self.play(
                ChangeDecimalToValue(number, stat["value"]),
                run_time=2,
                rate_func=linear
            )
            self.wait(0.5)

        self.wait(2)
        self.play(FadeOut(VGroup(title, stat_group)))


class TimelineAnimation(Scene):
    """Create timeline animation from CSV data"""

    def construct(self):
        # Sample timeline data
        events = [
            {"year": "2020", "event": "Project Started"},
            {"year": "2021", "event": "First Release"},
            {"year": "2022", "event": "Major Update"},
            {"year": "2023", "event": "Global Expansion"},
        ]

        # Title
        title = Text("Project Timeline", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Create timeline line
        timeline = Line(
            LEFT * 5 + DOWN * 0.5,
            RIGHT * 5 + DOWN * 0.5,
            color=BLUE,
            stroke_width=4
        )
        self.play(Create(timeline))
        self.wait(0.5)

        # Add events
        total_events = len(events)
        spacing = 10 / (total_events - 1)

        for i, event in enumerate(events):
            x_pos = -5 + i * spacing

            # Point on timeline
            dot = Dot([x_pos, -0.5, 0], color=YELLOW, radius=0.1)

            # Year
            year = Text(event["year"], font_size=28, color=YELLOW)
            year.move_to([x_pos, -1.2, 0])

            # Event description
            event_text = Text(event["event"], font_size=20, color=WHITE)
            event_text.move_to([x_pos, 0.5, 0])

            # Animate
            self.play(FadeIn(dot, scale=2))
            self.play(Write(year))
            self.play(FadeIn(event_text, shift=DOWN))
            self.wait(0.8)

        self.wait(2)
        self.play(FadeOut(*self.mobjects))


class CSVTableDisplay(Scene):
    """Display CSV data as animated table"""

    def construct(self):
        # Sample table data
        headers = ["Name", "Score", "Grade"]
        rows = [
            ["Alice", "95", "A"],
            ["Bob", "87", "B"],
            ["Charlie", "92", "A"],
            ["David", "78", "C"],
        ]

        # Title
        title = Text("Student Results", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Create table manually
        table_data = [headers] + rows

        table_group = VGroup()
        cell_width = 2.5
        cell_height = 0.6

        for row_idx, row in enumerate(table_data):
            row_group = VGroup()

            for col_idx, cell_text in enumerate(row):
                # Cell rectangle
                cell = Rectangle(
                    width=cell_width,
                    height=cell_height,
                    stroke_color=WHITE,
                    stroke_width=2
                )

                # Cell text
                text = Text(
                    cell_text,
                    font_size=24,
                    color=YELLOW if row_idx == 0 else WHITE
                )
                text.move_to(cell.get_center())

                cell_group = VGroup(cell, text)

                # Position
                x_pos = -3 + col_idx * cell_width
                y_pos = 1.5 - row_idx * cell_height

                cell_group.move_to([x_pos, y_pos, 0])
                row_group.add(cell_group)

            table_group.add(row_group)

            # Animate row appearance
            self.play(
                *[FadeIn(cell_group, shift=DOWN) for cell_group in row_group],
                run_time=0.5
            )

        self.wait(2)
        self.play(FadeOut(VGroup(title, table_group)))


def load_csv_data(csv_path):
    """
    Helper function to load data from CSV file
    Usage in Manim scenes:
        data = load_csv_data("data/questions.csv")
    """
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Warning: CSV file not found: {csv_path}")
        return []


if __name__ == "__main__":
    """
    Run this script to render all CSV data animations
    """
    import sys
    import subprocess

    script_file = sys.argv[0]
    scenes = [
        "CSVDataVisualization",
        "DynamicTextAnimation",
        "NumberAnimation",
        "TimelineAnimation",
        "CSVTableDisplay"
    ]

    for scene in scenes:
        print(f"\n{'='*50}")
        print(f"Rendering {scene}...")
        print('='*50)

        cmd = ["manim", "render", script_file, scene, "-qh"]
        subprocess.run(cmd)

    print("\n✓ All CSV data scenes rendered successfully!")
