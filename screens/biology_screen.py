from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.metrics import sp
from kivy.core.window import Window

from constants import (
    FONT_SCALE,
    PADDING_HORIZONTAL,
    PADDING_VERTICAL,
    SPACING_VERTICAL,
    BUTTON_HEIGHT_RATIO,
    BUTTON_FONT_RATIO
)


class ResponsiveButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, None)
        self.height = Window.height * BUTTON_HEIGHT_RATIO
        self.halign = 'center'
        self.valign = 'middle'
        self.shorten = False
        self.text_size = (self.width * 0.9, None)
        self.bind(size=self._update_font_size)
        Window.bind(size=self._update_font_size)

    def _update_font_size(self, *args):
        self.text_size = (self.width * 0.95, None)
        base = min(self.width, self.height)
        self.font_size = sp(base * BUTTON_FONT_RATIO * FONT_SCALE)


class BiologyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_class = None

        layout = BoxLayout(
            orientation='vertical',
            spacing=SPACING_VERTICAL,
            padding=[PADDING_HORIZONTAL, PADDING_VERTICAL]
        )

        study_btn = ResponsiveButton(text="📘 Study Material")
        study_btn.bind(on_press=self.open_study_material)

        quiz_btn = ResponsiveButton(text="🧪 Quiz")
        quiz_btn.bind(on_press=self.open_quiz)

        history_btn = ResponsiveButton(text="📊 History")
        history_btn.bind(on_press=self.open_history)

        layout.add_widget(study_btn)
        layout.add_widget(quiz_btn)
        layout.add_widget(history_btn)

        self.add_widget(layout)

    def open_study_material(self, instance):
        print("📘 Study Material Clicked")

    def open_quiz(self, instance):
        chapter_screen = self.manager.get_screen('chapter_list')
        chapter_screen.selected_class = self.selected_class
        chapter_screen.selected_subject = 'biology'
        self.manager.current = 'chapter_list'

    def open_history(self, instance):
        history_screen = self.manager.get_screen('history_screen')
        history_screen.selected_class = self.selected_class
        history_screen.selected_subject = 'biology'
        self.manager.current = 'history_screen'
