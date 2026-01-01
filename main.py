from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MainUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.lbl = Label(text="اپ پایتونی من", font_size=30)
        btn = Button(text="کلیک کن", size_hint=(1, 0.3))
        btn.bind(on_press=self.click)
        self.add_widget(self.lbl)
        self.add_widget(btn)

    def click(self, instance):
        self.lbl.text = "APK با موفقیت ساخته می‌شود 😎"

class MyApp(App):
    def build(self):
        return MainUI()

MyApp().run()
