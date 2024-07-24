from pages.registration_page import RegistrationForm

from test_data.user import User



def test_complete_todo():
    form_page = RegistrationForm()
    admin = User(first_name="Julia",
               last_name="Engineer",
               email="engineer@mail.ru",
               gender='Female',
               phone="8800555353",
               birthday="14 June,2001",
               subject="English",
               photo="woman-face.png",
               hobbies="Reading",
               address="Engineer, 14",
               state="NCR",
               city="Delhi")
    form_page.open()
    form_page.register(admin)
    form_page.should_exact_text(admin)