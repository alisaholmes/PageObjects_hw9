from test_module.module import RegistrationForm


def test_complete_todo():
    registration_form = RegistrationForm()
    registration_form.open()
    registration_form.element_type_first_name("Julia")
    registration_form.element_type_last_name("Engineer")
    registration_form.element_type_user_email("engineer@mail.ru")
    registration_form.element_click_gender()
    registration_form.element_type_user_number("8800555353")
    registration_form.element_click_birthday()
    registration_form.element_type_click_subjects()
    registration_form.element_click_hobbies()
    registration_form.element_picture("woman-face.png")
    registration_form.element_type_address("Engineer, 14")
    registration_form.element_type_state("NCR")
    registration_form.element_type_city("Delhi")
    registration_form.element_press_submit()
    registration_form.element_should_have_text("Thanks for submitting the form")
    registration_form.element_should_exact_text("Julia Engineer",
            "engineer@mail.ru",
            "Female",
            "8800555353",
            "14 June,2001",
            "English",
            "Reading",
            "woman-face.png",
            "Engineer, 14",
            "NCR Delhi")

