from kivy.app import App
from random import choice
from kivy.properties import ObjectProperty
from tic.player import Player
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
Window.size = 600, 300
Window.name = 'TICTACTOE'
x = 'X'
o = 'O'
matrix = [[7,8,9],[4,5,6],[1,2,3]]
name = ""
listaai = []

#kv file

Builder.load_string("""

<Menu>:
    canvas.before:
        Color:
            rgba: 0, 0, 255, 0.1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        orientation: 'vertical'

        Label:
            text: 'Jogo Da Velha' 
            font_size: '30sp'
            color: 128,0,128,0.9
        Button: 
            size: (300,50)
            size_hint: None, None
            text: 'Jogar'
            on_press: root.manager.current = 'game'
            #on_release: app.crialista()
            color: 128,0,128,0.9
            background_color: 0, 0, 255, 0.1
        Button: 
            size: (300,50)
            size_hint: None, None
            text: 'Sair'
            on_press: exit()
            color: 128,0,128,0.9
            background_color: 0, 0, 255, 0.1
            pos: (300, 0)
          
           
            
<Game>:
    canvas.before:
        Color:
            rgba: 0, 0, 255, 0.1
        Rectangle:
            pos: self.pos
            size: self.size

    canvas:
        Color:
            rgba: 255,255,255,255
        Rectangle:
            pos:
                (330,15)
            size:
                4,\
            230 
        Rectangle:
            pos:
                (255,15)
            size:
                4,\
            230
        Rectangle:
            pos:
                (255,15)
            size:
                4,\
            230
        Line:
            width: 3
            points: [180,95,405,95]
            joint: 'none'
            cap: 'square'
            close: False
        Line:
            width: 3
            points: [180,170,405,170]
            joint: 'none'
            cap: 'square'
            close: False
    FloatLayout:
        Label:
            text: 'Vamos Jogar:' 
            font_size: '20sp'
            color: 128,0,128,0.9
            pos: (0, 130)
        Button:
            text: 'Start'
            font_size: '15'
            color: 128,0,128,0.9
            size: (100,60)
            size_hint: None, None
            pos: (0, 0)
            on_press: root.crialista()
        Button:
            text: 'Restart'
            font_size: '15'
            color: 128,0,128,0.9
            size: (100,60)
            size_hint: None, None
            pos: (500,0)
            on_press: root.restart()
            
        Button:
            text: ''
            size: (70,70)
            size_hint: None, None
            pos: (185, 20)
            id: bt_1
            name : "bt1"
            on_press : root.name = 'bt1'
            on_release: root.preenche()
            
        Button:
            text: ''
            size: (70,70)
            size_hint: None, None
            pos: (185, 95)
            id: bt_2
            name: 'bt2'
            on_press : root.name = 'bt2'
            on_release: root.preenche()
        Button:
            text: ''
            size: (70,70)
            size_hint: None, None
            pos: (185, 170)
            id: bt_3
            on_press : root.name = 'bt3'
            on_release: root.preenche()
        Button:
            text: ''
            size: (70,70)
            size_hint: None, None
            pos: (260, 20)
            id: bt_4
            on_press : root.name = 'bt4'
            on_release: root.preenche()
        Button:
            text: ''
            size: (70,70)
            size_hint: None, None
            pos: (260,95)
            id: bt_5
            on_press : root.name = 'bt5'
            on_release: root.preenche()
        Button:
            text: ''
            size: (70,70)
            size_hint: None, None
            pos: (260, 170)
            id: bt_6
            on_press : root.name = 'bt6'
            on_release: root.preenche()
        Button:
            text: ''
            size: (70,70)
            size_hint: None, None
            pos: (335, 20)
            id: bt_7
            on_press : root.name = 'bt7'
            on_release: root.preenche()
        Button:
            text: ''
            size: (70,70)
            size_hint: None, None
            pos: (335, 95)
            id: bt_8
            on_press : root.name = 'bt8'
            on_release: root.preenche()
        Button:
            text: ''
            size: (70,70)
            size_hint: None, None
            pos: (335, 170)
            id: bt_9
            on_press : root.name = 'bt9'
            on_release: root.preenche()
            
        Label:
            text: 'Player1'
            font_size: '20'
            color: 128,0,128,0.9
            size: (100,60)
            size_hint: None, None
            pos: (0,150)
        Label:
            text: 'Player1'
            font_size: '20'
            color: 128,0,128,0.9
            size: (100,60)
            size_hint: None, None
            pos: (505,150)
        Button:
            text: ''
            font_size: '20'
            font_color: 192,192,192,0.8
            background_color: 0, 0, 255, 0.1
            size: (100,60)
            size_hint: None, None
            pos: (0,110)
            id: pl_1
        Button:
            text: ""
            font_size: '20'
            font_color: 192,192,192,0.8
            background_color: 0, 0, 255, 0.1
            size: (100,60)
            size_hint: None, None
            pos: (505,110)
            id: pl_2
            
            
""")

# Declare both screens
class Menu(Screen):
    pass

class Game(Screen):
    global name
    global x
    global o
    global matrix
    global listaai
    placar1 = 0
    placar2 = 0
    
    
    # Criacao de lista com ids dos texts da classe Game no kivy
    def crialista(self):

        for i in self.ids:
            listaai.append(i)


    # reinicio de jogo mantendo placar
    def restart(self):
        listaai.clear()
        for i in self.ids:
            listaai.append(i)

        for i in listaai:
            if "bt_" in i:
                self.ids[i].text = ""
        listaai.clear()

    #placares do CPU e do Player1

    def placarp(self, *args):
        self.placar1 += 1
        self.ids.pl_1.text = str(self.placar1)
    def placarcpu(self, *args):
        self.placar2 =+ 1
        self.ids.pl_2.text = str(self.placar2)


    # ai do cpu
    def ai(self):

        cpu = choice(listaai)
        print(cpu)

        if self.ids[cpu].text == "":
            self.ids[cpu].text = o
            listaai.remove(cpu)

            print(listaai)
        elif self.ids[cpu].text == x:
            listaai.remove(cpu)
            cpu = choice(listaai)
        elif self.ids[cpu].text == o:
            listaai.remove(cpu)
            cpu = choice(listaai)
        else:
            if self.ids[cpu].text == "":
                self.ids[cpu].text = o
                listaai.remove(cpu)



        if len(listaai) == 0:
            Game.restart(self)



    # main do jogo, atualizacao de placar e decisao de vencedor
    def jogatina(self, *args):


        if self.ids.bt_7.text == x and self.ids.bt_5.text== x and self.ids.bt_3.text == x:

            Game.placarp(self)
        elif self.ids.bt_7.text == o  and self.ids.bt_5.text == o and self.ids.bt_3.text == o:
            Game.placarcpu(self)
        elif self.ids.bt_1.text == x and self.ids.bt_5.text == x and self.ids.bt_9.text == x:
            Game.placarp(self)

        elif self.ids.bt_1.text == o and self.ids.bt_5.text == o and self.ids.bt_9.text == o:
            Game.placarcpu(self)
        elif self.ids.bt_1.text==x and self.ids.bt_4.text==x and self.ids.bt_7.text == x:
            Game.placarp(self)

        elif self.ids.bt_1.text==o and self.ids.bt_4.text==o and self.ids.bt_7.text == o:
            Game.placarcpu(self)
        elif self.ids.bt_2.text==x and self.ids.bt_5.text==x and self.ids.bt_8.text == x:
            Game.placarp(self)

        elif self.ids.bt_2.text==o and self.ids.bt_5.text==o and self.ids.bt_8.text == o:
            Game.placarcpu(self)
        elif self.ids.bt_3.text==x and self.ids.bt_6.text==x and self.ids.bt_9.text == x:
            Game.placarp(self)

        elif self.ids.bt_3.text==o and self.ids.bt_6.text==o and self.ids.bt_9.text == o:
            Game.placarcpu(self)
        elif self.ids.bt_7.text==x and self.ids.bt_8.text==x and self.ids.bt_9.text == x:
            Game.placarp(self)
        elif self.ids.bt_7.text==o and self.ids.bt_8.text==o and self.ids.bt_9.text == o:
            Game.placarcpu(self)
        elif self.ids.bt_4.text==x and self.ids.bt_5.text==x and self.ids.bt_6.text == x:
            Game.placarp(self)
        elif self.ids.bt_4.text==o and self.ids.bt_5.text==o and self.ids.bt_6.text == o:
            Game.placarcpu(self)
        elif self.ids.bt_1.text==x and self.ids.bt_2.text==x and self.ids.bt_3.text == x:
            Game.placarp(self)
        elif self.ids.bt_1.text==o and self.ids.bt_2.text==o and self.ids.bt_3.text == o:
            Game.placarcpu(self)

        if len(listaai) == 0:
            Game.restart(self)



    # jogadas do Player 1

    def preenche(self):



        if self.name == "bt1":
            if self.ids.bt_1.text == "" :
                self.ids.bt_1.text = x
                listaai.remove('bt_1')
                Game.ai(self)
                Game.jogatina(self)

        elif self.name == "bt2":
            if self.ids.bt_2.text == "":
                self.ids.bt_2.text = x
                listaai.remove('bt_2')
                Game.ai(self)
                Game.jogatina(self)

        elif self.name == "bt3":
            if self.ids.bt_3.text == "":
                self.ids.bt_3.text = x
                listaai.remove('bt_3')
                Game.ai(self)
                Game.jogatina(self)

        elif self.name == "bt4":
            if self.ids.bt_4.text == "":
                self.ids.bt_4.text = x
                listaai.remove('bt_4')
                Game.ai(self)
                Game.jogatina(self)

        elif self.name == "bt5":
            if self.ids.bt_5.text == "":
                self.ids.bt_5.text = x
                matrix[1][1] = x
                listaai.remove('bt_5')
                Game.ai(self)
                Game.jogatina(self)

        elif self.name == "bt6":
            if self.ids.bt_6.text == "":
                self.ids.bt_6.text = x
                matrix[1][2] = x
                listaai.remove('bt_6')
                Game.ai(self)
                Game.jogatina(self)

        elif self.name == "bt7":
            if self.ids.bt_7.text == "":
                self.ids.bt_7.text = x
                listaai.remove('bt_7')
                Game.ai(self)
                Game.jogatina(self)

        elif self.name == "bt8":
            if self.ids.bt_8.text == "":
                self.ids.bt_8.text = x
                listaai.remove('bt_8')
                Game.ai(self)
                Game.jogatina(self)

        elif self.name == "bt9":
            if self.ids.bt_9.text == "":
                self.ids.bt_9.text = x
                listaai.remove('bt_9')
                Game.ai(self)
                Game.jogatina(self)






# Create the screen manager
sm = ScreenManager()
sm.add_widget(Menu(name='menu'))
sm.add_widget(Game(name='game'))


class Tic(App):
    global listaai
    def build(self):

        return sm




Tic().run()
