from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class QuizApp(App):
    def build(self):
        return self.build_quiz_screen()
    
    def build_quiz_screen(self):
        self.score = 0
        layout = BoxLayout(orientation='vertical')
        title = Label(text="Quiz App")
        layout.add_widget(title)
        name_layout=GridLayout(cols=2,padding=[100,10,400,10])
    
        self.student_name = Label(text="Name: ")
        name_layout.add_widget(self.student_name)
        self.student_name_input = TextInput(hint_text="Enter your name", size_hint_y=None, height=40,size_hint_x=None,width=300)
        name_layout.add_widget(self.student_name_input)
        layout.add_widget(name_layout)
        # Question 1
        question1 = Label(text="1. Which is the red planet?", padding=[10, 0, 400, 10])
        layout.add_widget(question1)

        options = GridLayout(cols=2, padding=[100, 10, 400, 10])
        self.option_1 = CheckBox()
        lb_1 = Label(text="A.Earth", padding=[10, 10, 400, 10])
        options.add_widget(self.option_1)
        options.add_widget(lb_1)

        self.option_2 = CheckBox()
        lb_2 = Label(text="B.Uranus", padding=[10, 10, 400, 10])
        options.add_widget(self.option_2)
        options.add_widget(lb_2)

        self.option_3 = CheckBox()
        lb_3 = Label(text="C.Mars", padding=[10, 10, 400, 10])
        options.add_widget(self.option_3)
        options.add_widget(lb_3)
        layout.add_widget(options)

        # Question 2
        question2 = Label(text="2. Which is the fastest animal?", padding=[10, 10, 400, 10])
        layout.add_widget(question2)

        options_2 = GridLayout(cols=2, padding=[100, 10, 400, 10])
        self.option_a = CheckBox()
        lb_a = Label(text="A.Elephant", padding=[10, 10, 400, 10])
        options_2.add_widget(self.option_a)
        options_2.add_widget(lb_a)

        self.option_b = CheckBox()
        lb_b = Label(text="B.Cheetah", padding=[10, 10, 400, 10])
        options_2.add_widget(self.option_b)
        options_2.add_widget(lb_b)

        self.option_c = CheckBox()
        lb_c = Label(text="C.Lion", padding=[10, 10, 400, 10])
        options_2.add_widget(self.option_c)
        options_2.add_widget(lb_c)
        layout.add_widget(options_2)

        # Question 3
        question3 = Label(text="3. Which is the largest ocean?", padding=[10, 10, 400, 10])
        layout.add_widget(question3)

        options_3 = GridLayout(cols=2, padding=[100, 10, 400, 10])
        self.option_x = CheckBox()
        lb_x = Label(text="A.Pacific Ocean", padding=[50, 10, 400, 10])
        options_3.add_widget(self.option_x)
        options_3.add_widget(lb_x)

        self.option_y = CheckBox()
        lb_y = Label(text="B.Artic Ocean", padding=[50, 10, 400, 10])
        options_3.add_widget(self.option_y)
        options_3.add_widget(lb_y)

        self.option_z = CheckBox()
        lb_z = Label(text="C.Indian Ocean", padding=[50, 10, 400, 10])
        options_3.add_widget(self.option_z)
        options_3.add_widget(lb_z)
        layout.add_widget(options_3)

        # Submit and Score
        submit_button = Button(text="Submit", on_press=self.submit_quiz, size_hint_y=None, height=40)
        self.score_lbl = Label(text=f"Score: {self.score}", size_hint_y=None, height=40)

        layout.add_widget(submit_button)
        layout.add_widget(self.score_lbl)

        return layout

    def submit_quiz(self, instance):
        self.score = 0
        self.student_name_text = self.student_name_input.text.strip()
        if not self.student_name_text:
            self.score_lbl.text = "Please enter your name."
            return
        if not self.option_1.active and not self.option_2.active and self.option_3.active:
            self.score += 1
        if not self.option_a.active and self.option_b.active and not self.option_c.active:
            self.score += 1
        if self.option_x.active and not self.option_y.active and not self.option_z.active:
            self.score += 1

        self.score_lbl.text = f"Score: {self.score}"

        with open("C:/Users/LENOVO\Desktop/Tkinter/C29/quiz.txt","a") as f:
            f.write(f"{self.student_name_text},{self.score}\n")
            self.clear_data()

    def clear_data(self):
        self.student_name_input.text = ""
        self.option_1.active = False
        self.option_2.active = False
        self.option_3.active = False
        self.option_a.active = False
        self.option_b.active = False
        self.option_c.active = False
        self.option_x.active = False
        self.option_y.active = False
        self.option_z.active = False
       

if __name__ == '__main__':
    QuizApp().run()
