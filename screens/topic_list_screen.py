from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
import os
import json

class TopicListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_class = None
        self.selected_subject = None
        self.selected_chapter = None
        self.selected_chapter_name = None
        self.layout_built = False
        self.performance_data = {}  # Load/save from history file later

    def on_pre_enter(self):
        self.clear_widgets()
        self.build_ui()

    def get_topic_list(self, chapter_name):
        """Return list of topics from hardcoded or file data (later you can read from txt)"""
        chapter_topics = {
            "The Living World": [
                "Introduction", "1.1 DIVERSITY IN THE LIVING WORLD", "1.2 TAXONOMIC CATEGORIES"
            ],
            "Biological Classification": [
                "Introduction", "2.1 KINGDOM MONERA", "2.2 KINGDOM PROTISTA", "2.3 KINGDOM FUNGI",
                "2.4 KINGDOM PLANTAE", "2.5 KINGDOM ANIMALIA", "2.6 VIRUSES, VIROIDS, PRIONS AND LICHENS", "SUMMARY"
            ],
            "Plant Kingdom": [
                "Introduction", "3.1 ALGAE", "3.2 BRYOPHYTES", "3.3 PTERIDOPHYTES",
                "3.4 GYMNOSPERMS", "3.5 ANGIOSPERMS", "SUMMARY"
            ],
            "Animal Kingdom": [
                "4.1 BASIS OF CLASSIFICATION", "4.2 CLASSIFICATION OF ANIMALS",
                "Phylum–Chordata Classes(4.2.11.1 to 4.2.11.7)",
                "TABLE 4.2 Salient Features of Different Phyla in the Animal Kingdom", "SUMMARY"
            ]
            # Add more chapters and topics later
        }
        return chapter_topics.get(chapter_name, [])

    def build_ui(self):
        outer_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        scroll = ScrollView(size_hint=(1, 1))
    
        layout = GridLayout(cols=4, spacing=10, size_hint_y=None, padding=10)
        layout.bind(minimum_height=layout.setter('height'))
    
        def nice_label(text, bold=False):
            return Label(
                text=text,
                bold=bold,
                size_hint_y=None,
                height=50,
                text_size=(None, None),
                halign='left',
                valign='middle'
            )
    
        # Headers
        layout.add_widget(nice_label("Topic Name", bold=True))
        layout.add_widget(nice_label("Result", bold=True))
        layout.add_widget(nice_label("Performance", bold=True))
        layout.add_widget(nice_label("Action", bold=True))
    
        topics = self.get_topic_list(self.selected_chapter_name)
    
        for topic in topics:
            result = self.get_result(topic)
            performance = self.get_performance(result)
    
            layout.add_widget(nice_label(topic))
            layout.add_widget(nice_label(result))
            layout.add_widget(nice_label(performance))
    
            start_btn = Button(
                text="Start",
                size_hint_y=None,
                height=40,
                padding=[10, 10],
                halign='center'
            )
            start_btn.topic = topic
            start_btn.bind(on_press=self.start_quiz)
            layout.add_widget(start_btn)
    
        scroll.add_widget(layout)
        outer_layout.add_widget(scroll)
        self.add_widget(outer_layout)


    def get_result(self, topic):
        # Later: load from local storage
        return "Pending"

    def get_performance(self, result):
        try:
            score = int(result.replace("%", ""))
            if score == 100:
                return "Perfect"
            elif score >= 80:
                return "Moderate"
            else:
                return "Weak"
        except:
            return "Pending"

    def start_quiz(self, instance):
        topic = instance.topic
        quiz_screen = self.manager.get_screen('quiz')
        quiz_screen.selected_class = self.selected_class
        quiz_screen.selected_subject = self.selected_subject
        quiz_screen.selected_chapter = self.selected_chapter
        quiz_screen.selected_topic = topic
        quiz_screen.selected_chapter_name = self.selected_chapter_name
        self.manager.current = 'quiz'

    