from test_module.module import RegistrationForm
from test_module.users import User


def test_complete_todo():
    registration_form = RegistrationForm()
    user = User(first_name="Julia",
                last_name="Engineer",
                user_email="engineer@mail.ru",
                gender="Female",
                user_number="8800555353",
                birthday="14 June,2001",
                subject="English",
                hobbies="Reading",
                picture="woman-face.png",
                address="Engineer, 14",
                state="NCR",
                city="Delhi")

    registration_form.open()
    registration_form.register(user)
    registration_form.should_exact_text(user)
