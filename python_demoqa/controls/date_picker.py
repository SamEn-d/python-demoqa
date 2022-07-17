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


