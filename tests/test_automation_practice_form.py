from selene.support.shared import browser
from selene import command
from python_demoqa.controls.tags_input import TagsInput
from python_demoqa.controls.dropdown import Dropdown
from python_demoqa.controls import date_picker
from python_demoqa.controls.tablerow import TableRow
from python_demoqa.page.automation_practice_form_page import SetGender, SetInput,SetTextarea, Hobbies, Set
from python_demoqa.controls import upload

def browser_page_automation_practice_form():
    browser.open('automation-practice-form')
    browser.driver.set_window_size(width=1920, height=1080)

def test_automation_practice_form():
    #Given
    browser_page_automation_practice_form()

    #When
    SetInput('#firstName', 'Sam')
    SetInput('#lastName', 'End')
    SetInput('#userEmail', 'w@wth.su')
    SetInput('#userNumber', '8800755353')
    '''
    # OR
    Set.first_name('Sam')
    Set.last_name('End')
    Set.email('w@wth.su')
    Set.phone_number('8800755353')
    '''

    SetGender().male()

    date_picker.from_list('31', '6', '1990')

    Hobbies().sports().reading().music()

    upload.File('img.jpg')

    SetTextarea('#currentAddress', 'Mou" adress tak daleko chto хочется плакать')

    subjects = TagsInput()
    (subjects
     .add('Chem', autocomplete='Chemistry', css_class='.subjects-auto-complete__option')
     .add('Maths')
     .add('Physics')
     .press_enter('Arts')
     .press_tab('History')
    )

    Dropdown().set_in_list('Uttar Pradesh')
    Dropdown('#city').autocomplite('Lucknow')

    browser.element('#submit').perform(command.js.click)

    #Then
    result = TableRow
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
