from models.application import app


def test_complete_todo():
    app.left_panel.open()
    app.left_panel.type_first_name("Julia")
    app.left_panel.type_last_name("Engineer")
    app.left_panel.type_user_email("engineer@mail.ru")
    app.left_panel.gender()
    app.left_panel.type_number("8800555353")
    app.left_panel.birthday()
    app.left_panel.type_subjects("English")
    app.left_panel.hobbies()
    app.left_panel.picture("woman-face.png")
    app.left_panel.type_address("Engineer, 14")
    app.left_panel.type_state("NCR")
    app.left_panel.type_city("Delhi")
    app.left_panel.press_submit()
    app.left_panel.should_have_text("Thanks for submitting the form")
    app.left_panel.should_exact_text("Julia Engineer",
                                     "engineer@mail.ru",
                                     "Female",
                                     "8800555353",
                                     "14 June,2001",
                                     "English",
                                     "Reading",
                                     "woman-face.png",
                                     "Engineer, 14",
                                     "NCR Delhi")
