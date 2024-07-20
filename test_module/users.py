import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    gender: str
    user_number: str
    birthday: str
    subject: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str


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
