from selene import have
from selene.core.entity import SeleneElement, Element
from selene.support.shared import browser
from typing import Optional

element: SeleneElement = ...

class Dropdown():
    def __init__(self, id_class_parent: str = None ):
        self.id_class_parent = id_class_parent if id_class_parent else '#state'

    def autocomplite(self,name, search_text_id: Optional[str] = '[id^=react-select]'):
        browser.element(self.id_class_parent).element(search_text_id).type(name).press_tab()
        browser.element('#city').element('[id^=react-select-][id*=-input]').type('l').press_tab()

    def set_in_list(self, name, search_text_id: Optional[str] = '[id^=react-select]' ):
        browser.element(self.id_class_parent).click()
        browser.element(self.id_class_parent).all(search_text_id).element_by(have.text(name)).click()


