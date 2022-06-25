from selene.support.shared import browser
from selene import be, have, by
import pytest
import time #ssss

#переменные для test_automation_practice_form
# @pytest.fixture(scope='function')
def variables_automation_practice_form():
    browser.open('webtables')
    browser.driver.set_window_size(width=1920, height=1080)
    # browser.open('https://demoqa.com/automation-practice-form')
    # browser.open('https://demoqa.com/automation-practice-form').driver.maximize_window()
    # browser.execute_script("document.querySelector('#app > footer').remove")
    # browser.execute_script("document.querySelector('#app > footer').style.display='none'")
    # browser.execute_script("document.querySelectorAll('[id^=goolge-ads]').style.display='none'")

# def variables_other():
name = 'Sam'
lastname = 'End'
mail = 'w@wth.su'
age = '80'
salary = '19990'
department = 'Sports'

def repeat():
    browser.element('#userForm #firstName').set_value(name)
    browser.element('#userForm #lastName').set_value(lastname)
    browser.element('#userForm #userEmail').set_value(mail)
    browser.element('#userForm #age').set_value(age)
    browser.element('#userForm #salary').set_value(salary)
    browser.element('#userForm #department').set_value(department)
    browser.element('#userForm #submit').click()

def test_webtables():#variables_automation_practice_form):
    variables_automation_practice_form()

    #step1
    browser.element('#addNewRecordButton').click()
    repeat()

    #step2
    browser.element('#edit-record-2').click()
    repeat()

    #step3
    browser.element('#delete-record-3').click()

    # time.sleep(5) #Для отладки