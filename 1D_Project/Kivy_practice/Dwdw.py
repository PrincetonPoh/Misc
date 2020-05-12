import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.label import Label

in_color = 1,0,0,1
fbin1_value = 'DIRTY'
f = "full"
w = "wet"
s = "smelly"

class P(FloatLayout):
    pass

class MainWindow(Screen):
    btn_1 = ObjectProperty(None)
    fbin_1 = ObjectProperty(None)
    '''def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.btn_1.background_color = in_color'''

    def btn1(self):
        show = P()
        self.ids.fbin_1.text = 'bin 1: ' + fbin1_value
        popupWindow = Popup(title = 'Level 1', content=show, size_hint=(None,None), size=(400,400))
        #print(type(self.fbin_1))
        #self.fbin_1.text = 'bin 1: ' + fbin1_value
        popupWindow.open()

    def btn2(self):
        show = P()
        popupWindow = Popup(title = 'Level 2', content=Label(text=f'bin 4 is {f}, {w}, {s}\n \n bin 5 is {f}, {w} {s}\n \n bin 6 is {f}, {w}, {s}.'), size_hint=(None,None), size=(400,400))
        popupWindow.open()
        
    
    def btn3(self):
        show = P()
        popupWindow = Popup(title = 'Level 3', content=show, size_hint=(None,None), size=(400,400))
        popupWindow.open()

    def btn4(self):
        show = P()
        popupWindow = Popup(title = 'Level 4', content=show, size_hint=(None,None), size=(400,400))
        popupWindow.open()

    def btn5(self):
        show = P()
        popupWindow = Popup(title = 'Level 5', content=show, size_hint=(None,None), size=(400,400))
        popupWindow.open()

    def btn6(self):
        show = P()
        popupWindow = Popup(title = 'Level 6', content=show, size_hint=(None,None), size=(400,400))
        popupWindow.open()

    def btn7(self):
        show = P()
        popupWindow = Popup(title = 'Level 7', content=show, size_hint=(None,None), size=(400,400))
        popupWindow.open()
    
    def update(self):
        self.btn_1.background_color = in_color
        self.btn_1.text = 'surprise!!'
    
class SecondWindow(Screen):
    pass
    
class WindowManager(ScreenManager):
    pass

'''
def show_popup():
    show = P()
    popupWindow = Popup(title = 'Popup Window', content=show, size_hint=(None,None), size=(400,400))
    popupWindow.open()
'''

kv = Builder.load_file('Dwdw.kv')
class DwdwApp(App):
    def build(self):
        return kv

DwdwApp().run()

