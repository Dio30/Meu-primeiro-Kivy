from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout

class FormLogin(MDFloatLayout):
    def abrir_card(self):
        self.add_widget(SenhaCard())
        
class SenhaCard(MDCard):
    def fechar(self):
        self.parent.remove_widget(self)

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Cyan'
        self.theme_cls.primary_hue = '700'
        self.theme_cls.theme_style = 'Dark'
        return Builder.load_file(filename="main.kv")
    
MyApp().run()