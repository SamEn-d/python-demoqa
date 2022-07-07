from typing import Optional

from selene import browser, have
from selene.core.entity import Element, SeleneElement


element: SeleneElement = ...

class TagsInput:
    def __init__(self, elements: Element = None ):
        self.elements = elements if elements else browser.element('#subjectsInput')

    def add(self, from_: str, /, *, autocomplete: Optional[str] = None, css_class: Optional[str] = '.subjects-auto-complete__option'):
        self.elements.type(from_)
        browser.all(css_class).element_by(have.text(autocomplete or from_)).click()
        return self

    def press_enter(self,from_):
        self.elements.type(from_).press_enter()
        return self

    def press_tab(self,from_):
        self.elements.type(from_).press_tab()
        return self