from typing import Optional

from selene import by
from selene.core.entity import Element
from selene.support.shared import browser


class setInput():
    def __init__(self, element: Element = None, value: Optional = type):
        self.element = browser.element(element).type(value)

class setTextarea(setInput):
    ...


class setCheckboxBtn():
    def __init__(self,   element: Element = None, /, *, whatCheck: Optional[str] = None, ):
        self.element = browser.element(element).click()

class setCheckboxText():
    def __init__(self,   element: Element = None, /, *, whatCheck: Optional[str] = None, ):
        self.element = browser.element(by.text(element)).click()

class set():
    # def __init__(self, element: Element = None):
    #     self.element = browser.element(element).click()
    #     ...

    def first_name(self):
        browser.element('#firstName').type(self)

    def last_name(self):
        browser.element('#lastName').type(self)

    def email(self):
        browser.element('#userEmail').type(self)

    def phone_number(self):
        browser.element('#userNumber').type(self)