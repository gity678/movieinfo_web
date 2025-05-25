from kivy.app import App
from kivy.uix.label import Label

class MovieApp(App):
    def build(self):
        return Label(text='يرجى فتح التطبيق على المتصفح عبر http://127.0.0.1:5000')

if __name__ == '__main__':
    MovieApp().run()
