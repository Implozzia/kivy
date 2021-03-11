from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        return Button(text='CLICK!', background_color=[.11, .84, .58, 1], font_size=40, on_press=self.btn_press)

    def btn_press(self, instance):
        instance.text = 'ALREADY CLICK!'


if __name__ == "__main__":
    MyApp().run()
