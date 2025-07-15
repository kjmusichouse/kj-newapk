from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView

from utils.fetcher import fetch_quiz_json  # Use your GitHub fetch code

class QuizScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_class = None
        self.selected_subject = None
        self.selected_chapter = None
        self.selected_topic = None

        self.questions = []
        self.current_index = 0
        self.score = 0
        self.answers = []

    def on_enter(self):
        self.clear_widgets()
        self.load_quiz()

    def load_quiz(self):
        self.questions = fetch_quiz_json(
            cls=self.selected_class,
            subject=self.selected_subject,
            chapter=self.selected_chapter,
            topic=self.selected_topic
        )
        if not self.questions:
            self.add_widget(Label(text="No quiz available for this topic."))
            return
        self.current_index = 0
        self.score = 0
        self.answers = []
        self.show_question()

    def show_question(self):
        self.clear_widgets()
        if self.current_index >= len(self.questions):
            self.show_result()
            return

        q = self.questions[self.current_index]
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        question_label = Label(
            text=f"[b]Q{self.current_index + 1}. {q['question']}[/b]",
            markup=True,
            halign='left',
            valign='top',
            size_hint_y=None
        )
        question_label.bind(texture_size=question_label.setter('size'))
        layout.add_widget(question_label)

        self.selected_option = None  # Track selection

        for opt in q['options']:
            btn = Button(text=opt, size_hint_y=None, height=50)
            btn.bind(on_press=self.select_option)
            btn.correct_answer = q['answer']
            layout.add_widget(btn)

        # "Next" button
        next_button = Button(
            text="Next",
            size_hint_y=None,
            height=50
        )
        next_button.bind(on_press=self.on_next)
        layout.add_widget(next_button)

        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(layout)
        self.add_widget(scroll)

    def select_option(self, instance):
        self.selected_option = instance
        # Optional: highlight selected button (e.g., change color)
        for widget in instance.parent.children:
            if isinstance(widget, Button) and widget.text != "Next":
                widget.background_color = (1, 1, 1, 1)  # white
        instance.background_color = (0.5, 0.8, 1, 1)  # light blue

    def on_next(self, instance):
        if not self.selected_option:
            popup = Popup(
                title="No Option Selected",
                content=Label(text="Please select an option before proceeding."),
                size_hint=(0.6, 0.4)
            )
            popup.open()
            return

        selected = self.selected_option.text[0]  # e.g., "A. Option" -> "A"
        correct = self.selected_option.correct_answer

        self.answers.append({
            "question": self.questions[self.current_index]['question'],
            "selected": selected,
            "correct": correct,
            "options": self.questions[self.current_index]['options']
        })

        if selected == correct:
            self.score += 1

        self.current_index += 1
        self.show_question()




    #def check_answer(self, instance):
    #    selected = instance.text[0]  # e.g., "A. Option" -> "A"
    #    correct = instance.correct_answer
#
    #    self.answers.append({
    #        "question": self.questions[self.current_index]['question'],
    #        "selected": selected,
    #        "correct": correct,
    #        "options": self.questions[self.current_index]['options']
    #    })
#
    #    if selected == correct:
    #        self.score += 1
#
    #    self.current_index += 1
    #    Clock.schedule_once(lambda dt: self.show_question(), 0.2)

    def show_result(self):
        total = len(self.questions)
        percent = int((self.score / total) * 100)
        self.save_result(percent)

        result_screen = self.manager.get_screen('result')
        result_screen.percent = percent
        result_screen.answers = self.answers
        result_screen.total = total
        result_screen.correct = self.score
        result_screen.selected_topic = self.selected_topic
        result_screen.selected_chapter_name = self.selected_chapter_name  # ✅ Fix this

        self.manager.current = 'result'

    def save_result(self, percent):
        # Later: Save to file or db. For now, print.
        print(f"Saving result: {percent}% for {self.selected_topic}")
