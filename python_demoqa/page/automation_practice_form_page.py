from typing import Optional

from selene import by, have, command
from selene.core.entity import Element
from selene.support.shared import browser

from python_demoqa.controls import date_picker, upload
from python_demoqa.controls.dropdown import Dropdown
from python_demoqa.controls.tags_input import TagsInput

from selene.support.shared import browser
from selene import command, have




class Set():
    def first_name(self, name):
        browser.element('#firstName').type(name)
        return self

    def last_name(self, name):
        browser.element('#lastName').type(name)
        return self

    def email(self, mail):
        browser.element('#userEmail').type(mail)
        return self

    def phone_number(self, number):
        browser.element('#userNumber').type(number)
        return self

    def gender(self, gender):
        browser.element('#genterWrapper').all('label').element_by(have.exact_text(gender)).click()
        return self

    def birthdate(self, day, month, year):
        date_picker.from_list(day, month, year)
        return self


    def subjects(self, *subs):
        for set_subjects in subs:
            TagsInput().add(set_subjects)
        return self

    def hobbies(self, *hobbies):
        for select_hobbi in hobbies:
            browser.element('#hobbiesWrapper').all('label').element_by(have.exact_text(select_hobbi)).click()
        return self

    def picture(self, img):
        upload.File(img)
        return self

    def adress(self, adress):
        SetTextarea('#currentAddress', adress)
        return self

    def state(self, state):
        Dropdown().set_in_list(state)
        return self

    def city(self, city):
        Dropdown('#city').autocomplite(city)
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.click)


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
