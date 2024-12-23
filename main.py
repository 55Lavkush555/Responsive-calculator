from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        app_layout = BoxLayout(orientation="vertical")
        button_layout = GridLayout(rows=4)

        self.entry = TextInput(size_hint=[1, 0.2], font_size="25")
        
        
        self.btn = Button(text=btn_list[0], on_press=self.btn_click1)
        button_layout.add_widget(self.btn)
        self.btn = Button(text=btn_list[1], on_press=self.btn_click2)
        button_layout.add_widget(self.btn)
        self.btn = Button(text=btn_list[2], on_press=self.btn_click3)
        button_layout.add_widget(self.btn)
        self.btn = Button(text=btn_list[3], on_press=self.add)
        button_layout.add_widget(self.btn)
        self.btn = Button(text=btn_list[4], on_press=self.btn_click4)
        button_layout.add_widget(self.btn)
        self.btn = Button(text=btn_list[5], on_press=self.btn_click5)
        button_layout.add_widget(self.btn)
        self.btn = Button(text=btn_list[6], on_press=self.btn_click6)
        button_layout.add_widget(self.btn)
        self.btn = Button(text=btn_list[7], on_press=self.subtract)
        button_layout.add_widget(self.btn)
        self.btn = Button(text=btn_list[8], on_press=self.btn_click7)
        button_layout.add_widget(self.btn)
        self.btn = Button(text=btn_list[9], on_press=self.btn_click8)
        button_layout.add_widget(self.btn)
        self.btn = Button(text=btn_list[10], on_press=self.btn_click9)
        button_layout.add_widget(self.btn)
        self.btn = Button(text=btn_list[11], on_press=self.multiply)
        button_layout.add_widget(self.btn)
        self.btn = Button(text=btn_list[12], on_press=self.point)
        button_layout.add_widget(self.btn)
        self.btn = Button(text=btn_list[13], on_press=self.btn_click0)
        button_layout.add_widget(self.btn)
        self.btn = Button(text=btn_list[14], on_press=self.C)
        button_layout.add_widget(self.btn)
        self.btn = Button(text=btn_list[15], on_press=self.divide)
        button_layout.add_widget(self.btn)

                
        eq_btn = Button(text="=", size_hint=[1, 0.25], on_press=self.equal)

        app_layout.add_widget(self.entry)
        app_layout.add_widget(button_layout)
        app_layout.add_widget(eq_btn)
        return app_layout

    def btn_click1(self, obj):
        text = self.entry.text
        self.entry.text = text + '1'

    def btn_click2(self, obj):
        text = self.entry.text
        self.entry.text = text + '2'

    def btn_click3(self, obj):
        text = self.entry.text
        self.entry.text = text + '3'

    def btn_click4(self, obj):
        text = self.entry.text
        self.entry.text = text + '4'

    def btn_click5(self, obj):
        text = self.entry.text
        self.entry.text = text + '5'

    def btn_click6(self, obj):
        text = self.entry.text
        self.entry.text = text + '6'

    def btn_click7(self, obj):
        text = self.entry.text
        self.entry.text = text + '7'

    def btn_click8(self, obj):
        text = self.entry.text
        self.entry.text = text + '8'

    def btn_click9(self, obj):
        text = self.entry.text
        self.entry.text = text + '9'

    def btn_click0(self, obj):
        text = self.entry.text
        self.entry.text = text + '0'

    def point(self, obj):
        text = self.entry.text
        self.entry.text = text + '.'

    def add(self, obj):
        text = self.entry.text
        self.entry.text = text + '+'

    def subtract(self, obj):
        text = self.entry.text
        self.entry.text = text + '-'

    def multiply(self, obj):
        text = self.entry.text
        self.entry.text = text + '*'

    def divide(self, obj):
        text = self.entry.text
        self.entry.text = text + '/'

    def C(self, obj):
        self.entry.text = ''

    def equal(self, obj):
        text = self.entry.text
        try:
            self.entry.text = str(eval(text))
        except:
            self.entry.text = 'Wrong input!'

btn_list = ['1', '2', '3', '+',
            '4', '5', '6', '-', 
            '7', '8', '9', '*', 
            '.', '0', 'C', '/',]

app = CalculatorApp()
app.run()
