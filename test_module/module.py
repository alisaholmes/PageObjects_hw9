import os
from selene import browser, have


class RegistrationForm:
    def open(self):
        browser.open("/automation-practice-form")

    def element_type_first_name(self, first_name):
        browser.element("#firstName").type(first_name)
        pass

    def element_type_last_name(self, last_name):
        browser.element("#lastName").type(last_name)
        pass

    def element_type_user_email(self, user_email):
        browser.element("#userEmail").type(user_email)
        pass

    def element_click_gender(self):
        browser.element('[for="gender-radio-2"]').click()
        pass

    def element_type_user_number(self, user_number):
        browser.element("#userNumber").type(user_number)
        pass

    def element_click_birthday(self):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").type("2001").click()
        browser.element(".react-datepicker__month-select").element('[value="5"]').click()
        browser.element(".react-datepicker__day--014").click()
        pass

    def element_type_click_subjects(self):
        browser.element("#subjectsInput").type("English").click().press_enter()
        pass

    def element_click_hobbies(self):
        browser.element('[for="hobbies-checkbox-2"]').click()
        pass

    def element_picture(self, picture):
        browser.element("#uploadPicture").send_keys(os.path.abspath(picture))
        pass

    def element_type_address(self, address):
        browser.element("#currentAddress").type(address)
        pass

    def element_type_state(self, state):
        browser.element("#react-select-3-input").type(state).press_enter()
        pass

    def element_type_city(self, city):
        browser.element("#react-select-4-input").type(city).press_enter()
        pass

    def element_press_submit(self):
        browser.element("#submit").press_enter()
        pass

    def element_should_have_text(self, text):
        browser.element("#example-modal-sizes-title-lg").should(
            have.text(text))
        pass

    def element_should_exact_text(self, name, email, gender, number, birthday, subjects, hobbies, picture, address, city):
        browser.element(".table").all("td").even.should(
            have.exact_texts(
                "Julia Engineer",
                "engineer@mail.ru",
                "Female",
                "8800555353",
                "14 June,2001",
                "English",
                "Reading",
                "woman-face.png",
                "Engineer, 14",
                "NCR Delhi"
            )
        )
        pass

