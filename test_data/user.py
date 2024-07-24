class UserTextBox:
    name = str
    email = str
    current_address = str
    permanent_address = str

    def __init__(self, name, email, current_address, permanent_address):
        self.name = name
        self.email = email
        self.current_address = current_address
        self.permanent_address = permanent_address


user_text_box = UserTextBox("Julia Engineer",
                            "engineer@mail.ru",
                            "Engineer, 14",
                            "Engineer, 14")
