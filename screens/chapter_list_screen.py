from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.metrics import sp


class ResponsiveLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.halign = 'center'
        self.valign = 'middle'
        self.shorten = False
        self.bind(size=self._update_all)
        Window.bind(size=self._update_all)
        self._update_all()

    def _update_all(self, *args):
        self.text_size = (self.width * 0.95, self.height)
        self.font_size = sp(self.width * 0.05)  # Scale with width
        self.height = self.font_size * 2  # Adjust label height to fit text


class ResponsiveButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.halign = 'center'
        self.valign = 'middle'
        self.shorten = False
        self.bind(size=self._update_all)
        Window.bind(size=self._update_all)
        self._update_all()

    def _update_all(self, *args):
        self.text_size = (self.width * 0.95, self.height)
        self.font_size = sp(self.width * 0.05)  # Scale with width
        self.height = self.font_size * 2.2  # Button height based on font

class ChapterListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_class = None
        self.selected_subject = None
        self.layout_built = False

    def on_enter(self):
        if not self.layout_built:
            self.build_ui()
            self.layout_built = True

    def get_units_and_chapters(self):
        return {
            "UNIT I - DIVERSITY IN THE LIVING WORLD": {
                "1": "The Living World",
                "2": "Biological Classification",
                "3": "Plant Kingdom",
                "4": "Animal Kingdom"
            },
            "UNIT II - STRUCTURAL ORGANISATION IN PLANTS AND ANIMALS": {
                "5": "Morphology of Flowering Plants",
                "6": "Anatomy of Flowering Plants",
                "7": "Structural Organisation in Animals"
            },
            "UNIT III - CELL : STRUCTURE AND FUNCTIONS": {
                "8": "Cell : The Unit of Life",
                "9": "Biomolecules",
                "10": "Cell Cycle and Cell Division"
            },
            "UNIT IV - PLANT PHYSIOLOGY": {
                "11": "Photosynthesis in Higher Plants",
                "12": "Respiration in Plants",
                "13": "Plant Growth and Development"
            },
            "UNIT V - HUMAN PHYSIOLOGY": {
                "14": "Breathing and Exchange of Gases",
                "15": "Body Fluids and Circulation",
                "16": "Excretory Products and their Elimination",
                "17": "Locomotion and Movement",
                "18": "Neural Control and Coordination",
                "19": "Chemical Coordination and Integration"
            }
        }

    def build_ui(self):
        scroll = ScrollView()
        outer_layout = BoxLayout(orientation='vertical', padding=10)
        grid = GridLayout(cols=2, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        units = self.get_units_and_chapters()

        for unit_title, chapters in units.items():
            # Unit title row
            grid.add_widget(ResponsiveLabel(text=unit_title, bold=True))
            grid.add_widget(ResponsiveLabel(text=""))

            # Headings
            grid.add_widget(ResponsiveLabel(text="Chapter No.", bold=True))
            grid.add_widget(ResponsiveLabel(text="Chapter Name", bold=True))

            # Chapters
            for number, name in chapters.items():
                grid.add_widget(ResponsiveLabel(text=number))
                btn = ResponsiveButton(text=name)
                btn.chapter_number = number
                btn.chapter_name = name
                btn.bind(on_press=self.on_chapter_selected)
                grid.add_widget(btn)

        scroll.add_widget(grid)
        outer_layout.add_widget(scroll)
        self.add_widget(outer_layout)

    def on_chapter_selected(self, instance):
        selected_chapter = instance.chapter_number
        selected_chapter_name = instance.chapter_name

        topic_screen = self.manager.get_screen('topic_list')
        topic_screen.selected_class = self.selected_class
        topic_screen.selected_subject = self.selected_subject
        topic_screen.selected_chapter = selected_chapter
        topic_screen.selected_chapter_name = selected_chapter_name

        self.manager.current = 'topic_list'
