from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class SubjectScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_class = None

        layout = BoxLayout(orientation='vertical', spacing=20, padding=40)
        for subject in ['PHYSICS', 'CHEMISTRY', 'BIOLOGY']:
            btn = Button(text=subject, font_size=24)
            btn.bind(on_press=self.on_subject_selected)
            layout.add_widget(btn)

        self.add_widget(layout)

    def on_subject_selected(self, instance):
        subject = instance.text.upper()
        if subject == 'BIOLOGY':
            self.manager.get_screen('biology').selected_class = self.selected_class
            self.manager.current = 'biology'
        else:
            pass  # Can show "Coming Soon" or do nothing
