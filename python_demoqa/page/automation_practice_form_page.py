from typing import Optional

from selene import by, have
from selene.core.entity import Element
from selene.support.shared import browser


class SetInput():
    def __init__(self, element: str = None, value: Optional = type):
        self.element = browser.element(element).type(value)

class SetTextarea(SetInput):
    ...

class Hobbies():
    def __init__(self):
        self.element = browser.element('#hobbiesWrapper').all('label')
    def sports(self):
        self.element.element_by(have.exact_text('Sports')).click()
        # browser.element(have.exact_text('Sports')).click()
        return self

    def reading(self):
        self.element.element_by(have.exact_text('Reading')).click()
        # browser.element(have.exact_text('Reading')).click()
        return self

    def music(self):
        self.element.element_by(have.exact_text('Music')).click()
        # browser.element(have.exact_text('Music')).click()
        return self

class Set():
    def first_name(self):
        browser.element('#firstName').type(self)

    def last_name(self):
        browser.element('#lastName').type(self)

    def email(self):
        browser.element('#userEmail').type(self)

    def phone_number(self):
        browser.element('#userNumber').type(self)

class SetGender():
    def __init__(self):
        self.params = browser.element('#genterWrapper').all('label')

    def male(self):
        self.params.element_by(have.exact_text('Male')).click()
        return self

    def female(self):
        self.params.element_by(have.exact_text('Female')).click()
        return self

    def other(self):
        self.params.element_by(have.exact_text('Other')).click()
        return self
