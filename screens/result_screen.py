from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import json
import os
from datetime import datetime

#=========================================================================================
def save_quiz_result(topic, result, performance, chapter):
    history_path = "data/history.json"

    # Create file if it doesn't exist
    if not os.path.exists(history_path):
        with open(history_path, "w") as f:
            json.dump([], f)

    with open(history_path, "r") as f:
        history = json.load(f)

    history.append({
        "topic": topic,
        "chapter": chapter,  # ✅ Include chapter
        "result": result,
        "performance": performance,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

    with open(history_path, "w") as f:
        json.dump(history, f, indent=2)

#=================================================================================================

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.percent = 0
        self.correct = 0
        self.total = 0
        self.answers = []
        self.selected_topic = ""
        self.selected_chapter_name = ""  # ✅ New attribute

    def on_enter(self):
        self.clear_widgets()

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        result_label = Label(
            text=f"[b]Result: {self.correct} / {self.total}[/b]\nPercentage: {self.percent}%",
            markup=True,
            font_size='20sp'
        )

        # Performance tag
        if self.percent == 100:
            performance = "Perfect"
        elif self.percent >= 80:
            performance = "Moderate"
        else:
            performance = "Weak"

        performance_label = Label(
            text=f"Performance: [b]{performance}[/b]",
            markup=True,
            font_size='18sp'
        )

        result_text = f"{self.correct}/{self.total}"

        # ✅ Save result with chapter info
        save_quiz_result(
            topic=self.selected_topic,
            chapter=self.selected_chapter_name,  # ✅ add this
            result=result_text,
            performance=performance,
            #chapter=self.selected_chapter
        )

        review_btn = Button(text="Review Answers", size_hint=(1, 0.2))
        review_btn.bind(on_press=self.goto_review)

        layout.add_widget(result_label)
        layout.add_widget(performance_label)
        layout.add_widget(review_btn)

        self.add_widget(layout)

    def goto_review(self, instance):
        review_screen = self.manager.get_screen("review")
        review_screen.answers = self.answers
        review_screen.total = self.total
        review_screen.selected_topic = self.selected_topic
        self.manager.current = "review"
