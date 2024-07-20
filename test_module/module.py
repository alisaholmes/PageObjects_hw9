import os

from selene import browser, have

from test_module.users import User


class RegistrationForm:
    def open(self):
        browser.open("/automation-practice-form")

    def element_type_first_name(self, first_name):
        browser.element("#firstName").type(first_name)

    def element_type_last_name(self, last_name):
        browser.element("#lastName").type(last_name)

    def element_type_user_email(self, user_email):
        browser.element("#userEmail").type(user_email)

    def element_click_gender(self):
        browser.element('[for="gender-radio-2"]').click()

    def element_type_user_number(self, user_number):
        browser.element("#userNumber").type(user_number)

    def element_click_birthday(self):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").type("2001").click()
        browser.element(".react-datepicker__month-select").element('[value="5"]').click()
        browser.element(".react-datepicker__day--014").click()

    def element_type_click_subjects(self):
        browser.element("#subjectsInput").type("English").click().press_enter()

    def element_click_hobbies(self):
        browser.element('[for="hobbies-checkbox-2"]').click()

    def element_picture(self, picture):
        browser.element("#uploadPicture").send_keys(os.path.abspath(picture))

    def element_type_address(self, address):
        browser.element("#currentAddress").type(address)

    def element_type_state(self, state):
        browser.element("#react-select-3-input").type(state).press_enter()

    def element_type_city(self, city):
        browser.element("#react-select-4-input").type(city).press_enter()

    def element_press_submit(self):
        browser.element("#submit").press_enter()

    def element_should_have_text(self, text):
        browser.element("#example-modal-sizes-title-lg").should(
            have.text(text))

    def should_exact_text(self, user: User):
        browser.element(".table").all("td").even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                f'{user.user_email}',
                f'{user.gender}',
                f'{user.user_number}',
                f'{user.birthday}',
                f'{user.subject}',
                f'{user.hobbies}',
                f'{user.picture}',
                f'{user.address}',
                f'{user.state} {user.city}')
        )

    def register(self, user: User):
        self.element_type_first_name(user.first_name)
        self.element_type_last_name(user.last_name)
        self.element_type_user_email(user.user_email)
        self.element_click_gender()
        self.element_type_user_number(user.user_number)
        self.element_click_birthday()
        self.element_type_click_subjects()
        self.element_click_hobbies()
        self.element_picture(user.picture)
        self.element_type_address(user.address)
        self.element_type_state(user.state)
        self.element_type_city(user.city)
        self.element_press_submit()
