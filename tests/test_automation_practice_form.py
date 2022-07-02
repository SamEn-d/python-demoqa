from selene.support.shared import browser
from selene import be, have, by, command



def browser_page_automation_practice_form():
    browser.open('automation-practice-form')
    browser.driver.set_window_size(width=1920, height=1080)
    '''
    # Это нужно для скрытия элемента, сейчас решение через js клик
    browser.execute_script("document.querySelector('#app > footer').style.display='none'")
    '''

def test_automation_practice_form():
    #Given
    browser_page_automation_practice_form()

    class Hobbies:
        music = 'Music'
        sports = 'Sports'
        reading = 'Reading'

    class Student:
        name = 'Sam'
        lastname = 'End'
        mail = 'w@wth.su'
        mobile_number = '8800755353'
        subjects = ['English', 'Physics']
        address = 'Mou" adress tak daleko chto хочется плакать'
        day = '10'
        year = '1990'

    #When
    browser.element('#firstName').type(Student.name)
    browser.element('#lastName').type(Student.lastname)
    browser.element('#userEmail').type(Student.mail)

    gender_male = browser.element('[for="gender-radio-1"]')
    gender_male.click()

    browser.element('#userNumber').type(Student.mobile_number)

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select [value="0"]').click()
    browser.element(f'.react-datepicker__year-select [value="{Student.year}"]').click()
    browser.element(f'.react-datepicker__month .react-datepicker__week .react-datepicker__day--0{Student.day}').click()


    english = browser.element('#subjectsInput').set_value(Student.subjects[0])
    english.press_enter()

    physics = browser.element('#subjectsInput').set_value(Student.subjects[1])
    physics.press_tab()

    hobbies_music = browser.element('[for="hobbies-checkbox-1"]')
    hobbies_music.click()
    hobbies_sports = browser.element('[for="hobbies-checkbox-2"]')
    hobbies_sports.click()
    hobbies_reading = browser.element('[for="hobbies-checkbox-3"]')
    hobbies_reading.click()
    '''
    # OR
    browser.element(by.text(Hobbies.music)).click() # browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element(by.text(Hobbies.sports)).click() # browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element(by.text(Hobbies.reading)).click() # browser.element('[for="hobbies-checkbox-3"]').click()
    '''
    # print(upload_file_name('img.jpg'))
    # browser.element('#uploadPicture')#.perform(upload_file_name('imgsss.jpg'))

    browser.element('#uploadPicture').send_keys(resource('img.jpg'))

    # browser.element('#uploadPicture').send_keys(
    #     resource('pexels-vinicius-vieira-ft-3151954.jpg')
    # )

    browser.element('#currentAddress').type(Student.address)
    uttar_pradesh = browser.element('#react-select-3-option-1')
    browser.element('#state').click()
    uttar_pradesh.click()

    lucknow = browser.element('#city #react-select-4-option-1')
    browser.element('#city').click()
    lucknow.click()

    browser.element('#submit').perform(command.js.click)


    #Then
    def table_row_selector_search(number):
        return browser.element('.table').all('tr')[number].element('td:nth-child(2)')
        '''
        #OR
        return browser.element('.table tbody').element(f'tr:nth-child({number}').element('td:nth-child(2)')
        '''

    table_row_selector_search(1).should(have.exact_text(f'{Student.name} {Student.lastname}'))
    table_row_selector_search(2).should(have.exact_text(Student.mail))
    table_row_selector_search(3).should(have.exact_text('Male'))
    table_row_selector_search(4).should(have.exact_text(Student.mobile_number))
    table_row_selector_search(5).should(have.exact_text(f'{Student.day} January,{Student.year}'))
    table_row_selector_search(6).should(have.exact_text(f'{Student.subjects[0]}, {Student.subjects[1]}'))
    table_row_selector_search(7).should(have.exact_text(f'{Hobbies.sports}, {Hobbies.reading}, {Hobbies.music}'))
    table_row_selector_search(8).should(have.exact_text('img.jpg'))
    table_row_selector_search(9).should(have.exact_text(Student.address))
    table_row_selector_search(10).should(have.exact_text('Uttar Pradesh Lucknow'))

def resource(relative_path):
    import python_demoqa
    from pathlib import Path
    return (
        Path(python_demoqa.__file__)
        .parent
        .parent
        .joinpath('resources/')
        .joinpath(relative_path)
        .absolute()
        .__str__()
    )
