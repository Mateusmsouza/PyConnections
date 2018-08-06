#!/usr/bin/env python
from kivy.app import App
from kivy.uix.label import Label
from convert import ToolKitms
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.checkbox import CheckBox


import random
from lxml import etree
import pyperclip

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '350')
Config.set('graphics','resizable',0)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.write()



class Home(App):
    # this is the builder method
    def build(self):

        self.accumulate = False
        self.accumulated = None

        main_window = BoxLayout(orientation='vertical', size=(10,10)) # main window
        main_window.add_widget(Label(text='PyConnections', pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(None,100), font_size='80sp'))

        containt_box = GridLayout(cols=1, padding=10, spacing=20,
                size_hint=(None, None))

        containt_box.bind(minimum_height=containt_box.setter('height'))


        tempos = self.__intertools() # calling the method that read conections.txt file

        check_acumula_tempo = CheckBox(size_hint_y=None)
        check_acumula_tempo.bind(active=self.on_activate)

        #adding times using looping
        botao = []
        for index, tempo in enumerate(tempos):

            botao.append(Button(text=tempo, size = (800,40), size_hint=(None,None)))
            botao[index].bind(on_press= self.alter_time)
            containt_box.add_widget(botao[index])



        view_temp = ScrollView(size_hint=(None, None), size=(800, 200),
                pos_hint={'center_x': .5, 'center_y': .0}, do_scroll_x=False)

        view_temp.add_widget(containt_box)
        main_window.add_widget(check_acumula_tempo)
        main_window.add_widget(view_temp)
        return main_window

    def on_activate(self, checkbox, value):
        if value:
            self.accumulate = True
        else:
            self.accumulate = False
            self.accumulated = None

            egg = random.randint(1,3)
            if egg == 1: pyperclip.copy("Genilada")
            elif egg == 2: pyperclip.copy("HÁ UM SELO ESCONDIDO NO CARTÓRIO!")
            elif egg == 3: pyperclip.copy("sublê, sublê, substabelecimento!")

    # this will copy the time to ctrl + v
    def alter_time(self, instance):
        text = instance.text
        slice_y = text.find('[')

        # check if the time isn't broken
        if slice_y == -1 :
            pyperclip.copy(text)
            return

        # acumulate time
        if self.accumulate:
            ToolKit = ToolKitms()
            self.accumulated = ToolKit.add(self.accumulated,text[slice_y +1: slice_y+9])

        # send result to ctrl + v
        pyperclip.copy(text[slice_y +1: slice_y+9])
        return




    # back ground methods #
    def __intertools(self):
        ToolKit = ToolKitms()
        linhas = list()
        to_return = list()

        path = etree.parse(r'Path.xml')
        #path = etree.parse('Path.xml')
        path = etree.tostring(path, method="text")


        arquivo = open(path, 'r')
        for linha in arquivo:
            linhas.append(linha)
        arquivo.close()

        for i in linhas:
            palavras = i.split(" ")

            palavras = [a for a in palavras if
                        a != '' and a != '\n']  # Creating a new list from palavras, iterating and checking if x is
                        # different from ''
            print(palavras)
            if len(palavras) > 0: to_return.append(ToolKit.converte(palavras))

        return to_return




if __name__ == "__main__":
    Home = Home()
    Home.run()
