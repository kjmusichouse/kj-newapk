from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
from kivy.utils import platform

# Importing all screens
from screens.home_screen import HomeScreen
from screens.subject_screen import SubjectScreen
from screens.biology_screen import BiologyScreen
from screens.chapter_list_screen import ChapterListScreen
from screens.topic_list_screen import TopicListScreen
from screens.quiz_screen import QuizScreen
from screens.result_screen import ResultScreen
from screens.review_screen import ReviewScreen
from screens.history_screen import HistoryScreen


class QuizApp(App):
    def build(self):
        self.sm = ScreenManager(transition=SlideTransition())
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(SubjectScreen(name='subject'))
        self.sm.add_widget(BiologyScreen(name='biology'))
        self.sm.add_widget(ChapterListScreen(name='chapter_list'))
        self.sm.add_widget(ChapterListScreen(name='chapter_list_screen'))
        self.sm.add_widget(TopicListScreen(name='topic_list'))
        self.sm.add_widget(QuizScreen(name='quiz'))
        self.sm.add_widget(ResultScreen(name='result'))
        self.sm.add_widget(ReviewScreen(name='review'))
        self.sm.add_widget(HistoryScreen(name='history_screen'))

        return self.sm

    def on_start(self):
        # Bind back button only on Android or desktop keyboard (for testing)
        if platform in ('android', 'win', 'linux', 'macos'):
            Window.bind(on_keyboard=self.on_back_button)

    def on_back_button(self, window, key, *args):
        # key == 27 is the Back key on Android or ESC on desktop
        if key == 27:
            current = self.sm.current
            # Navigation logic
            if current != 'home':
                self.go_back_screen(current)
                return True  # handled
            else:
                return False  # exit app

    def go_back_screen(self, current):
        # You can customize screen-to-screen back navigation here
        back_map = {
            'subject': 'home',
            'biology': 'subject',
            'chapter_list': 'biology',
            'chapter_list_screen': 'biology',
            'topic_list': 'chapter_list',
            'quiz': 'topic_list',
            'result': 'topic_list',
            'review': 'history_screen',
            'history_screen': 'home'
        }

        previous = back_map.get(current, 'home')
        self.sm.transition.direction = 'right'
        self.sm.current = previous


if __name__ == '__main__':
    QuizApp().run()
