from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
SUBJECT_LIST = ["Math", "Science", "English", "Computer"]
class StudentApp(App):
    def build(self):
        return self.build_form_screen()

    def build_form_screen(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # --- Form Inputs ---
        form = GridLayout(cols=2, spacing=10, row_force_default=True, row_default_height=40)

        self.name_input = TextInput()
        self.age_input = TextInput(input_filter='int')
        self.gender_spinner = Spinner(text='Select', values=['Male', 'Female'])
        self.class_input = TextInput()
        self.address_input = TextInput()

        form.add_widget(Label(text="Name:"))
        form.add_widget(self.name_input)
        form.add_widget(Label(text="Age:"))
        form.add_widget(self.age_input)
        form.add_widget(Label(text="Gender:"))
        form.add_widget(self.gender_spinner)
        form.add_widget(Label(text="Class/Grade:"))
        form.add_widget(self.class_input)
        form.add_widget(Label(text="Address:"))
        form.add_widget(self.address_input)
        layout.add_widget(form)

        layout.add_widget(Label(text="Select Subjects:", size_hint_y=None, height=30))
       
       
  
        grid_layout = GridLayout(cols=2,padding=[400,0,400,0])
        self.cb_math = CheckBox()
        lb_math = Label(text="Math")
        grid_layout.add_widget(self.cb_math)
        grid_layout.add_widget(lb_math)

        self.cb_english = CheckBox()
        lb_english = Label(text="English")
        grid_layout.add_widget(self.cb_english)
        grid_layout.add_widget(lb_english)

        self.cb_science = CheckBox()
        lb_science = Label(text="Science")  
        grid_layout.add_widget(self.cb_science)
        grid_layout.add_widget(lb_science)

        self.cb_computer = CheckBox()
        lb_computer = Label(text="Computer")
        grid_layout.add_widget(self.cb_computer)
        grid_layout.add_widget(lb_computer)


        layout.add_widget(grid_layout)
       
        
        # --- Buttons & Status ---
        self.status_label = Label(text="", font_size=16, size_hint_y=None, height=40, markup=True)
        submit_btn = Button(text="Submit", size_hint_y=None, height=50)
       
       
        layout.add_widget(submit_btn)
        layout.add_widget(self.status_label)

        
        return layout




if __name__ == '__main__':
    StudentApp().run()
