from distutils.cmd import Command

from selene.support.shared import browser
from selene import be, have, by, command
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
    # browser.execute_script("document.querySelector('#app > footer').style.display='none'")
    # browser.execute_script("document.querySelectorAll('[id^=goolge-ads]').style.display='none'")

def test_automation_practice_form():#variables_automation_practice_form):
    #Given
    def tr_table_search(number_tr):
        return f'.table-responsive tbody tr:nth-child({number_tr}) td:nth-child(2)'

    class Hobbies:
        music = 'Music'
        sports = 'Sports'
        reading = 'Reading'

    class Student:
        name = 'Sam'
        lastname = 'End'
        mail = 'w@wth.su'
        number = '8800755353'
        subjectsInput = ['English', 'Physics']
        address = 'Mou" adress tak daleko chto хочется плакать'
        day = '10'
        year = '1990'

    variables_automation_practice_form()

    #When
    browser.element('#firstName').should(be.blank).type(Student.name)
    browser.element('#lastName').should(be.blank).type(Student.lastname)
    browser.element('#userEmail').should(be.blank).type(Student.mail)

    browser.element('#gender-radio-1')
    browser.element('[for="gender-radio-1"]').click()

    browser.element('#userNumber').should(be.blank).type(Student.number)

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select [value="0"]').click()
    browser.element(f'.react-datepicker__year-select [value="{Student.year}"]').click()
    browser.element(f'.react-datepicker__month .react-datepicker__week .react-datepicker__day--0{Student.day}').click()
    browser.element('#subjectsInput').should(be.blank).set_value(Student.subjectsInput[0]).press_enter()
    browser.element('#subjectsInput').should(be.blank).set_value(Student.subjectsInput[1]).press_enter()

    browser.element(by.text(Hobbies.music)).click() # browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element(by.text(Hobbies.sports)).click() # browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element(by.text(Hobbies.reading)).click() # browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('#uploadPicture')

    browser.element('#currentAddress').should(be.blank).type(Student.address)

    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city').click()
    browser.element('#city #react-select-4-option-1').click()
    # browser.element('#uploadPicture').send_keys('/img.jpg')
    # browser.element('#submit').click()
    browser.element('#submit').perform(command.js.click)
    # browser.element('.table-responsive tbody').element('//tr[1]/td[2]').should(have.exact_text(name + ' ' + lastname))

    #Than
    browser.element(tr_table_search(1)).should(have.exact_text(f'{Student.name} {Student.lastname}'))
    browser.element(tr_table_search(2)).should(have.exact_text(Student.mail))
    browser.element(tr_table_search(3)).should(have.exact_text('Male'))
    browser.element(tr_table_search(4)).should(have.exact_text(Student.number))
    browser.element(tr_table_search(5)).should(have.exact_text(f'{Student.day} January,{Student.year}'))
    browser.element(tr_table_search(6)).should(have.exact_text(Student.subjectsInput[0] + ', ' + Student.subjectsInput[1]))
    browser.element(tr_table_search(7)).should(have.exact_text(f'{Hobbies.music}, {Hobbies.sports}, {Hobbies.reading}'))
    browser.element(tr_table_search(8)).should(have.exact_text(f''))
    browser.element(tr_table_search(9)).should(have.exact_text(Student.address))
    browser.element(tr_table_search(10)).should(have.exact_text('Uttar Pradesh Lucknow'))



#Old code
    # browser.element('.table-responsive tbody tr:nth-child(1) td:nth-child(2)').should(have.exact_text(f'{Student.name} {Student.lastname}'))
    # table_tr.element('//tr[1]/td[2]').should(have.exact_text(f'{Student.name} {Student.lastname}'))
    # table_tr.element('//tr[2]/td[2]').should(have.exact_text(Student.mail))
    # table_tr.element('//tr[3]/td[2]').should(have.exact_text('Male'))
    # table_tr.element('//tr[4]/td[2]').should(have.exact_text(Student.number))
    # table_tr.element('//tr[6]/td[2]').should(have.exact_text(Student.subjectsInput[0] + ', ' + Student.subjectsInput[1]))
    # table_tr.element('//tr[7]/td[2]').should(have.exact_text(f'{Hobbies.music}, {Hobbies.sports}, {Hobbies.reading}'))
    # table_tr.element('//tr[9]/td[2]').should(have.exact_text(Student.address))
    # table_tr.element('//tr[10]/td[2]').should(have.exact_text('Uttar Pradesh Lucknow'))
    # table_tr.element('//tr[5]/td[2]').should(have.exact_text(f'{Student.day} January,{Student.year}'))
    # browser.element('#closeLargeModal').click()
    # browser.element('#closeLargeModal').click()
    # time.sleep(5) #Для отладки