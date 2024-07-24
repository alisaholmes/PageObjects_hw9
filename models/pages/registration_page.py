from pathlib import Path

from selene import browser, have


class RegistrationForm:
    def open(self):
        browser.open("/automation-practice-form")

    def type_first_name(self, first_name):
        browser.element("#firstName").type(first_name)

    def type_last_name(self, last_name):
        browser.element("#lastName").type(last_name)

    def type_user_email(self, email):
        browser.element('#userEmail').type(email)

    def gender(self):
        browser.element('[for="gender-radio-2"]').click()

    def type_number(self, phone):
        browser.element('#userNumber').type(phone)

    def birthday(self):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").type("2001").click()
        browser.element(".react-datepicker__month-select").element('[value="5"]').click()
        browser.element(".react-datepicker__day--014").click()

    def type_subjects(self, subject):
        browser.element("#subjectsInput").type(subject).click().press_enter()

    def hobbies(self):
        browser.element('[for="hobbies-checkbox-2"]').click()

    def picture(self, photo):
        browser.element('#uploadPicture').send_keys(str(Path(__file__).parent.parent.joinpath(f'resources/{photo}')))

    def type_address(self, address):
        browser.element('#currentAddress').type(address)

    def type_state(self, state):
        browser.element("#react-select-3-input").type(state).press_enter()

    def type_city(self, city):
        browser.element("#react-select-4-input").type(city).press_enter()

    def press_submit(self):
        browser.element("#submit").press_enter()

    def should_have_text(self, text):
        browser.element("#example-modal-sizes-title-lg").should(have.text(text))

    def should_exact_text(self, first_name, email, gender, phone, birthday, subjects, hobbies, photo, address, city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(first_name, email, gender, phone, birthday, subjects, hobbies, photo, address, city))

    def open_simple_registration_form(self):
        browser.open('/text-box')
