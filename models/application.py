from models.pages.registration_page import RegistrationForm
from models.pages.text_box_page import TextBoxForm


class AppManager:
    def __init__(self):
        self.text_box_form = TextBoxForm()
        self.left_panel = RegistrationForm()


app = AppManager()