from selene.support.shared import browser
from selene import be, have, by, command
from python_demoqa.controls import path_to_directory
from python_demoqa.controls.tags_input import TagsInput
from python_demoqa.controls.dropdown import Dropdown
from python_demoqa.controls import date_picker
from python_demoqa.controls.table import Table

def browser_page_automation_practice_form():
    browser.open('automation-practice-form')
    browser.driver.set_window_size(width=1920, height=1080)

def test_automation_practice_form():
    #Given
    browser_page_automation_practice_form()

    #When
    browser.element('#firstName').set_value('Sam')
    browser.element('#lastName').type('End')
    browser.element('#userEmail').type('w@wth.su')

    gender_male = browser.element('[for="gender-radio-1"]')
    gender_male.click()

    mobile_number = browser.element('#userNumber')
    mobile_number.type('8800755353')

    date_picker.set_to_js('31 Jul 1980')
    '''
    # OR
    # date_picker.from_list('20', '4','1990')
    '''

    hobbies_music = browser.element('[for="hobbies-checkbox-1"]')
    hobbies_music.click()
    hobbies_sports = browser.element('[for="hobbies-checkbox-2"]')
    hobbies_sports.click()
    hobbies_reading = browser.element('[for="hobbies-checkbox-3"]')
    hobbies_reading.click()
    '''
    # OR
    browser.element(by.text(Hobbies.music)).click()
    browser.element(by.text(Hobbies.sports)).click()
    browser.element(by.text(Hobbies.reading)).click()
    '''

    browser.element('#uploadPicture').send_keys(path_to_directory.filename('img.jpg'))

    browser.element('#currentAddress').type('Mou" adress tak daleko chto хочется плакать')

    subjects = TagsInput()
    subjects.add('Chem', autocomplete='Chemistry', css_class='.subjects-auto-complete__option')
    subjects.add('Maths')
    subjects.press_enter('Arts')
    subjects.press_tab('History')


    dropdown_state = Dropdown()
    dropdown_state.set_in_list('Uttar Pradesh')

    dropdown_city = Dropdown('#city')
    dropdown_city.autocomplite('Lucknow')

    browser.element('#submit').perform(command.js.click)

    #Then

    Table.row_selector(1, value='Sam End')
    Table.row_selector(2, value='w@wth.su')
    Table.row_selector(3, value='Male')
    Table.row_selector(4, value='8800755353')
    Table.row_selector(5, value='07 July,2022')
    Table.row_selector(6, value='Chemistry, Maths, Arts, History')
    Table.row_selector(7, value='Sports, Reading, Music')
    Table.row_selector(8, value='img.jpg')
    Table.row_selector(9, value='Mou" adress tak daleko chto хочется плакать')
    Table.row_selector(10, value='Uttar Pradesh Lucknow')