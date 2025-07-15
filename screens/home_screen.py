from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.metrics import sp

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


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            spacing=SPACING_VERTICAL,
            padding=[PADDING_HORIZONTAL, PADDING_VERTICAL]
        )

        for cls in ['Class 10', 'Class 11', 'Class 12']:
            btn = ResponsiveButton(text=cls)
            btn.bind(on_press=self.on_class_selected)
            layout.add_widget(btn)

        self.add_widget(layout)

    def on_class_selected(self, instance):
        selected_class = instance.text.split()[-1]
        self.manager.get_screen('subject').selected_class = selected_class
        self.manager.current = 'subject'
