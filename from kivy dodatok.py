from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.image import Image

inst = '''Всім привіт! Сьогодні я вам покажу додаток на подобі програми про рибалку, у ньому ви можете дізнатися про 
багатьох відомих риб, які проживають у річках України:
1 - Карась звичайний
2 - Короп 
3 - Білий амур 
4 - Лящ 
5 - Сом 
6 - Щука'''

class Main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        green = (.15, .20, .05, .5)
        Window.clearcolor = green
        image = Image(source="image.jpg")

        lineV = FloatLayout(size_hint=(1, 1))
        line1 = BoxLayout(size_hint=(1, 0.4), pos_hint={"y": 0.7, "center_x": 0.5})
        line2 = BoxLayout(size_hint=(0.5, 0.05), pos_hint={"y": 0.4, "center_x": 0.5})
        line4 = BoxLayout(size_hint=(0.25, 0.1), pos_hint={"y": 0, "center_x": 0.5})

        label1 = Label(text=inst, halign="center", valign="middle")
        label1.bind(size=label1.setter('text_size'))
        line1.add_widget(label1)
        line1.add_widget(image)

        label2 = Label(text="Введіть номер риби, про яку ви хочете дізнатися", halign="center")
        self.age = TextInput(multiline=False)
        line2.add_widget(label2)
        line2.add_widget(self.age)
        red = (.255, .0, .0, 1)

        but1 = Button(text="Інформація", background_color=red)
        anim = Animation(background_color=(0, 0, 1, 1), font_size=60, duration=3.5)
        anim2 = Animation(font_size=60, duration=3.5)
        anim3 = anim + anim2
        anim3.start(but1)

        line4.add_widget(but1)

        lineV.add_widget(line1)
        lineV.add_widget(line2)
        lineV.add_widget(line4)

        self.add_widget(lineV)
        but1.on_press = self.next_win1  

    def next_win1(self):
        global new_age
        age_text = self.age.text.strip()
        if age_text.isdigit():
            new_age = int(age_text)
            self.manager.current = 'main2'
            self.manager.transition.direction = "up"
        else:
            print("Помилка: введіть правильне число.")

class Main2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.info_labels = {
            1: "Карась звичайний:\n\n"
               "Середовище: Стоячі або повно текучі водою з густою рослинністю.\n"
               "Харчування: Водості, дрібні безхребетні, комахи.\n"
               "Способи ловлі: На черв'яка, мотиля, кукурудзу; активний вранці і ввечері.",
            2: "Короп:\n\n"
               "Середовище: Річки і ставки.\n"
               "Харчування: Всеїдний, різноманітний раціон.\n"
               "Способи ловлі: Найактивніший у ранкові та вечірні години.",
            3: "Білий амур:\n\n"
               "Середовище: Чисті та проточні води з багатою рослинністю.\n"
               "Харчування: В основному рослинна їжа, водорості.\n"
               "Способи ловлі: На траву, горох, кукурудзу.",
            4: "Лящ:\n\n"
               "Середовище: Повільні річки та стоячі водойми.\n"
               "Харчування: Безхребетні, донні організми, водорості.\n"
               "Способи ловлі: На хробака, мотиля, опариша.",
            5: "Сом:\n\n"
               "Середовище: Глибокі річки та озера.\n"
               "Харчування: Дрібні риби, жаби, ракоподібні.\n"
               "Способи ловлі: На живця, риб'ячий шматок, кальмара; активний уночі.",
            6: "Щука:\n\n"
               "Середовище: Чисті прісноводні водойми.\n"
               "Харчування: Дрібні риби, земноводні.\n"
               "Способи ловлі: На блешню, воблер, живця."
        }

        self.info_label = Label(size_hint=(1, 0.6), text="", halign="left", valign="top")
        self.info_label.bind(size=self.info_label.setter('text_size'))

        self.image = Image(size_hint=(1, 0.4), source="", pos_hint={"y": 0})
        

        lineF = BoxLayout(orientation="vertical")
        lineF.add_widget(self.image)
        lineF.add_widget(self.info_label)

        #Назад
        back_button = Button(text="Назад", size_hint=(0.2, 0.1), pos_hint={"center_x": 0.5})
        back_button.bind(on_press=self.go_back)
        lineF.add_widget(back_button)

        self.add_widget(lineF)

    def on_enter(self):
        fish_info = self.info_labels.get(new_age, "Невірний номер риби")
        fish_images = {
            1: "kr.jpg",
            2: "korop.jpg",
            3: "amyr.jpg",
            4: "lach.jpg",
            5: "com.jpg",
            6: "ch.jpg"
        }
        self.info_label.text = fish_info
        
        self.image.source = fish_images.get(new_age, "") 

    def go_back(self, *args):
        self.manager.current = 'main'
        self.manager.transition.direction = "down"

class Win(App):
    def build(self):
        main_screen = ScreenManager()
        main_screen.add_widget(Main(name='main'))
        main_screen.add_widget(Main2(name='main2'))
        return main_screen

app = Win()
app.run()




