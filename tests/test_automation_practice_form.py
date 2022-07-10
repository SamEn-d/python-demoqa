from selene.support.shared import browser
from selene import command
from python_demoqa.controls.tags_input import TagsInput
from python_demoqa.controls.dropdown import Dropdown
from python_demoqa.controls import date_picker
from python_demoqa.controls.table import Table
from python_demoqa.page.automation_practice_form_page import setInput, setCheckboxBtn,setTextarea, setCheckboxText, set
from python_demoqa.controls import upload

def browser_page_automation_practice_form():
    browser.open('automation-practice-form')
    browser.driver.set_window_size(width=1920, height=1080)

def test_automation_practice_form():
    #Given
    browser_page_automation_practice_form()

    #When


    setInput('#firstName', 'Sam')
    setInput('#lastName', 'End')
    setInput('#userEmail', 'w@wth.su')
    setInput('#userNumber', '8800755353')
    '''
    # OR
    set.first_name('Sam')
    set.last_name('End')
    set.email('w@wth.su')
    set.phone_number('8800755353')
    '''

    setCheckboxBtn('[for="gender-radio-1"]', whatCheck='Male')

    date_picker.from_list('31', '6', '1990')
    '''
    # OR
    date_picker.set_to_js('31 Jul 1980')
    '''

    setCheckboxBtn('[for="hobbies-checkbox-1"]', whatCheck='Хобби Sports')
    setCheckboxBtn('[for="hobbies-checkbox-2"]', whatCheck='Хобби Reading')
    setCheckboxBtn('[for="hobbies-checkbox-3"]', whatCheck='Хобби Music')
    '''
    # OR
    setCheckboxText('Sports', whatCheck='Хобби Music')
    setCheckboxText('Reading', whatCheck='Хобби Music')
    setCheckboxText('Music', whatCheck='Хобби Music')
    '''

    upload.File('img.jpg')

    setTextarea('#currentAddress', 'Mou" adress tak daleko chto хочется плакать')

    subjects = TagsInput()
    subjects.add('Chem', autocomplete='Chemistry', css_class='.subjects-auto-complete__option')
    subjects.add('Maths').add('Physics').press_enter('Arts').press_tab('History')

    Dropdown().set_in_list('Uttar Pradesh')
    Dropdown('#city').autocomplite('Lucknow')

    browser.element('#submit').perform(command.js.click)

    #Then
    result = Table
    result.row_selector(1, value='Sam End')
    result.row_selector(2, value='w@wth.su')
    result.row_selector(3, value='Male')
    result.row_selector(4, value='8800755353')
    result.row_selector(5, value='31 July,1990')
    result.row_selector(6, value='Chemistry, Maths, Physics, Arts, History')
    result.row_selector(7, value='Sports, Reading, Music')
    result.row_selector(8, value='img.jpg')
    result.row_selector(9, value='Mou" adress tak daleko chto хочется плакать')
    result.row_selector(10, value='Uttar Pradesh Lucknow')