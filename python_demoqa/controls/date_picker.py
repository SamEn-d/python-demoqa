from selene import command
from selene.core.entity import Element
from selene.support.shared import browser

def from_list(day, month, year, ):
    browser.element('#dateOfBirthInput').click()
    browser.element(f'.react-datepicker__month-select [value="{month}"]').click()
    browser.element(f'.react-datepicker__year-select [value="{year}"]').click()
    browser.element(f'.react-datepicker__month .react-datepicker__week .react-datepicker__day--0{day}').click()

def set_to_js(date):
    browser.element('#dateOfBirthInput').perform(command.js.set_value(date))

class DatePicker:
    def __init__(self, element: Element = None ):
        self.element = element.click()

    def select_year(self, year):
        browser.element(f'.react-datepicker__year-select [value="{year}"]').click()
        return self

    def select_month(self, month):
        browser.element(f'.react-datepicker__month-select [value="{month}"]').click()
        return self

    def select_day(self, day):
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def set_to_js(self, date):
        browser.element('div').click()
        set_to_js(date)

