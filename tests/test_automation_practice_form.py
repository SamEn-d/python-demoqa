from selene.support.shared import browser
from selene import command
from python_demoqa.controls.tags_input import TagsInput
from python_demoqa.controls.dropdown import Dropdown
from python_demoqa.controls import date_picker
from python_demoqa.controls.tablerow import TableRow
from python_demoqa.page.automation_practice_form_page import SetInput, SetCheckboxBtn,SetTextarea, SetCheckboxText, Set
from python_demoqa.controls import upload
from python_demoqa.controls.date_picker import DatePicker

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

    SetCheckboxBtn('[for="gender-radio-1"]', whatCheck='Male')

    date_picker.from_list('31', '6', '1990')
    '''
    # OR
    date_picker.set_to_js('31 Jul 1980')
    
    # Мама сказала что нужно сделать по ООП :(
    #OR 
    birth_date = DatePicker(browser.element('#dateOfBirthInput'))
    birth_date.select_year(1990).select_month(6).select_day(31) 
    #OR
    DatePicker(browser.element('#dateOfBirthInput')).set_to_js('31 Jul 1990')
    '''


    # calendar = '#dateOfBirthInput'
    # browser.element(calendar).click()
    # date_of_birth = DatePicker(browser.element('#dateOfBirth'))
    # date_of_birth.select_year(1989).select_month(Months.August).select_day(15)
    # # date_of_birth.set_date(calendar, '15 Aug 1989')

    SetCheckboxBtn('[for="hobbies-checkbox-1"]', whatCheck='Хобби Sports')
    SetCheckboxBtn('[for="hobbies-checkbox-2"]', whatCheck='Хобби Reading')
    SetCheckboxBtn('[for="hobbies-checkbox-3"]', whatCheck='Хобби Music')
    '''
    # OR
    setCheckboxText('Sports', whatCheck='Хобби Music')
    setCheckboxText('Reading', whatCheck='Хобби Music')
    setCheckboxText('Music', whatCheck='Хобби Music')
    '''

    upload.File('img.jpg')

    SetTextarea('#currentAddress', 'Mou" adress tak daleko chto хочется плакать')

    subjects = TagsInput()
    subjects.add('Chem', autocomplete='Chemistry', css_class='.subjects-auto-complete__option')
    subjects.add('Maths').add('Physics').press_enter('Arts').press_tab('History')

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
