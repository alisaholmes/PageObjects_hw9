from pages.registration_page import RegistrationForm


def test_complete_todo():
    registration_form = RegistrationForm()
    registration_form.open()
    registration_form.type_first_name("Julia")
    registration_form.type_last_name("Engineer")
    registration_form.type_user_email("engineer@mail.ru")
    registration_form.gender()
    registration_form.type_number("8800555353")
    registration_form.birthday()
    registration_form.type_subjects()
    registration_form.hobbies()
    registration_form.picture("woman-face.png")
    registration_form.type_address("Engineer, 14")
    registration_form.type_state("NCR")
    registration_form.type_city("Delhi")
    registration_form.press_submit()
    registration_form.should_have_text("Thanks for submitting the form")
    registration_form.should_exact_text("Julia Engineer",
                                        "engineer@mail.ru",
                                        "Female",
                                        "8800555353",
                                        "14 June,2001",
                                        "English",
                                        "Reading",
                                        "woman-face.png",
                                        "Engineer, 14",
                                        "NCR Delhi")
