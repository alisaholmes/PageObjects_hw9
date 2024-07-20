from selene import browser, have
from test_module.users import UserTextBox

class TextBoxFrom:
    def open(self):
        browser.open('text-box/')

    def fill_name(self, value):
        browser.element('#userName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def fill_current_address(self, current_address):
        browser.element('#currentAddress').type(current_address).press_enter()
        return self

    def fill_permanent_address(self, permanent_address):
        browser.element('#permanentAddress').type(permanent_address).press_enter()
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def register_text_box(self, user: UserTextBox):
        self.type_name(user.name)
        self.type_email(user.email)
        self.type_current_address(user.current_address)
        self.type_permanent_address(user.permanent_address)
        self.submit_form()
        return self

    def should_register_info(self, user: UserTextBox):
        browser.element('#output').should(have.exact_text(f'Name:{user.name}\n'
                                                          f'Email:{user.email}\n'
                                                          f'Current Address :{user.current_address}\n'
                                                          f'Permanent Address :{user.permanent_address}'))
