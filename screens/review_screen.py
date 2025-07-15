from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp, sp
from datetime import datetime
import json
import os

class ReviewScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.answers = []
        self.total = 0
        self.selected_topic = ""
        self.history_entries = []

    def on_enter(self):
        self.clear_widgets()

        layout = BoxLayout(orientation='vertical', padding=10)
        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        # Topic title if available
        if self.selected_topic:
            grid.add_widget(Label(
                text=f"[b][color=ffffff]{self.selected_topic}[/color][/b]",
                markup=True,
                font_size=sp(20),
                size_hint_y=None,
                height=dp(40),
                halign='center',
                valign='middle'
            ))

        # 1. If quiz answers available – show that
        if self.answers:
            for idx, ans in enumerate(self.answers, 1):
                question_text = ans['question']
                selected_letter = ans['selected']
                correct_letter = ans['correct']
                options = ans['options']

                selected_index = ord(selected_letter) - ord('A')
                correct_index = ord(correct_letter) - ord('A')

                selected_text = options[selected_index] if 0 <= selected_index < len(options) else "N/A"
                correct_text = options[correct_index] if 0 <= correct_index < len(options) else "N/A"

                is_correct = selected_letter == correct_letter
                status_text = "CORRECT" if is_correct else "INCORRECT"
                status_color = "00ff00" if is_correct else "ff3333"

                text = f"[color=ffffff][b]{question_text}[/b][/color]\n"
                text += f"[color=ffff00]Your Answer:[/color] [color=ffffff]{selected_text}[/color] [color={status_color}]{status_text}[/color]\n"

                if not is_correct:
                    text += f"[color=00ff00]Correct Answer:[/color] [color=ffffff]{correct_text}[/color]"

                row = Label(
                    text=text,
                    markup=True,
                    size_hint_y=None,
                    height=dp(130),
                    halign='left',
                    valign='top'
                )
                row.bind(size=row.setter('text_size'))
                grid.add_widget(row)

        # 2. Else if history entries available – show summary
        elif self.history_entries:
            for entry in self.history_entries:
                try:
                    date_obj = datetime.strptime(entry['date'], "%Y-%m-%d %H:%M")
                    formatted_date = date_obj.strftime("%d-%m-%Y %I:%M %p")
                except:
                    formatted_date = entry['date']

                result = entry['result']
                performance = entry['performance']

                text = (
                    f"[color=ffffff][b]Result:[/b][/color] [color=ffcc00]{result}[/color]    "
                    f"[color=ffffff][b]Performance:[/b][/color] [color=ffffff]{performance}[/color]    "
                    f"[color=00ffff][b]Date:[/b][/color] [color=ffffff]{formatted_date}[/color]"
                )

                label = Label(
                    text=text,
                    markup=True,
                    font_size=sp(14),
                    size_hint_y=None,
                    height=dp(40),
                    halign='left',
                    valign='middle'
                )
                label.bind(size=label.setter('text_size'))
                grid.add_widget(label)

        else:
            grid.add_widget(Label(
                text="[color=ff0000]No review data available.[/color]",
                markup=True,
                font_size=sp(16),
                size_hint_y=None,
                height=dp(30)
            ))

        scroll.add_widget(grid)
        layout.add_widget(scroll)
        self.add_widget(layout)

    def load_topic_from_history(self,chapter_name, topic_name):
        """Call this from history screen"""
        self.selected_topic = topic_name
        self.answers = []  # Clear quiz answers
        self.history_entries = []

        history_file = 'data/history.json'
        if os.path.exists(history_file):
            with open(history_file, 'r') as f:
                history = json.load(f)
                self.history_entries = [h for h in reversed(history) if h['topic'] == topic_name]
