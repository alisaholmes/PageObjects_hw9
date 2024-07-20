
from test_module import users
from test_module.application import app


def test_text_box():
    app.text_box.open_text_box_form()
    app.text_box.register_text_box(users.user_text_box)
    app.text_box.should_register_info(users.user_text_box)