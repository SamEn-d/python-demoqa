from typing import Optional

from selene import have
from selene.core.entity import Element
from selene.support.shared import browser

class TableRow():
    def __init__(self, element: Element = None, css_class: Optional[str] = None, tr: Optional[str] = None ):
        self.element = browser.element(css_class).all(tr) if css_class and tr else browser.element('.table').all('tr')

    def row_selector(number, /, *, value):
        browser.element('.table').all('tr')[number].element('td:nth-child(2)').should(have.exact_text(value))
