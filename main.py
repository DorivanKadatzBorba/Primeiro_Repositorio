#Author: Dorivan Kadatz Borba

from kivy.app import App
from kivy.uix.screenmanager import Screen


# Classe para compor os widgets do arquivo meu.kv
class RootWidget(Screen):
    pass


# Classe principal do App
class MeuApp(App):
    def build(self):
        return RootWidget() # Retorna os objetos compostos na classe RootWidget


if __name__ == "__main__":  # Inicia o Aplicativo
    MeuApp().run()
