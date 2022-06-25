from selene.support.shared import browser
from selene import be, have, by
import pytest
import time #ssss

#переменные для test_automation_practice_form
# @pytest.fixture(scope='function')
def variables_automation_practice_form():
    browser.open('automation-practice-form')
    browser.driver.set_window_size(width=1920, height=1080)
    # browser.open('https://demoqa.com/automation-practice-form')
    # browser.open('https://demoqa.com/automation-practice-form').driver.maximize_window()
    # browser.execute_script("document.querySelector('#app > footer').remove")
    browser.execute_script("document.querySelector('#app > footer').style.display='none'")
    # browser.execute_script("document.querySelectorAll('[id^=goolge-ads]').style.display='none'")

# def variables_other():
name = 'Sam'
lastname = 'End'
mail = 'w@wth.su'
number = '8800755353'
subjectsInput = ['English', 'Physics']
address = 'Mou" adress tak daleko chto хочется плакать'
day = '10'
year = '1990'
music = 'Music'
Sports = 'Sports'
Readin = 'Reading'

def test_automation_practice_form():#variables_automation_practice_form):
    variables_automation_practice_form()

    browser.element('#firstName').should(be.blank).type(name)
    browser.element('#lastName').should(be.blank).type(lastname)
    browser.element('#userEmail').should(be.blank).type(mail)
    browser.element('#gender-radio-1')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type(number)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select [value="0"]').click()
    browser.element(f'.react-datepicker__year-select [value="{year}"]').click()
    browser.element(f'.react-datepicker__month .react-datepicker__week .react-datepicker__day--0{day}').click()
    browser.element('#subjectsInput').should(be.blank).set_value(subjectsInput[0]).press_enter()
    browser.element('#subjectsInput').should(be.blank).set_value(subjectsInput[1]).press_enter()
    browser.element(by.text(music)).click()
    browser.element(by.text(Sports)).click()
    browser.element(by.text(Readin)).click()
    # browser.element('[for="hobbies-checkbox-1"]').click()
    # browser.element('[for="hobbies-checkbox-2"]').click()
    # browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture')
    browser.element('#currentAddress').should(be.blank).type(address)
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city').click()
    browser.element('#city #react-select-4-option-1').click()
    # browser.element('#uploadPicture').send_keys('img.jpg')
    browser.element('#submit').click()

    browser.element('.table-responsive tbody').element('//tr[1]/td[2]').should(have.exact_text(name + ' ' + lastname))
    browser.element('.table-responsive tbody').element('//tr[2]/td[2]').should(have.exact_text(mail))
    browser.element('.table-responsive tbody').element('//tr[3]/td[2]').should(have.exact_text('Male'))
    browser.element('.table-responsive tbody').element('//tr[4]/td[2]').should(have.exact_text(number))
    browser.element('.table-responsive tbody').element('//tr[6]/td[2]')\
        .should(have.exact_text(subjectsInput[0] + ', ' + subjectsInput[1]))
    browser.element('.table-responsive tbody').element('//tr[7]/td[2]').should(have.exact_text(f'{music}, {Sports}, {Readin}'))
    browser.element('.table-responsive tbody').element('//tr[9]/td[2]').should(have.exact_text(address))
    browser.element('.table-responsive tbody').element('//tr[10]/td[2]').should(have.exact_text('Uttar Pradesh Lucknow'))
    browser.element('.table-responsive tbody').element('//tr[5]/td[2]').should(have.exact_text(f'{day} January,{year}'))
    browser.element('#closeLargeModal').click()
    # time.sleep(5) #Для отладки