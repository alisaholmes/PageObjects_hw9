from test_module.module import RegistrationForm
from test_module import TextBoxFrom

class Application:
    def __init__(self):
        self.registration = RegistrationForm()
        self.text_box = TextBoxFrom()



app = Application()