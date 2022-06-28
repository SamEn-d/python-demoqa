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

    #Сделать иначе сабджект
    # ['English', 'Physics']
    english = browser.element('#subjectsInput').set_value(Student.subjects[0])
    english.press_enter()

    physics = browser.element('#subjectsInput').set_value(Student.subjects[1])
    physics.press_tab()
    #
    # english = browser.element('#subjectsInput').set_value(Student.subjectsInput[0]).press_enter()
    # physics = browser.element('#subjectsInput').set_value(Student.subjectsInput[1]).press_enter()
    # browser.element('#subjectsInput').set_value(Student.subjectsInput[0]).press_enter()
    # browser.element('#subjectsInput').set_value(Student.subjectsInput[1]).press_enter()

    #Сделать как за решеткой но сделать понятные переменные
    browser.element(by.text(Hobbies.music)).click() # browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element(by.text(Hobbies.sports)).click() # browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element(by.text(Hobbies.reading)).click() # browser.element('[for="hobbies-checkbox-3"]').click()
    # print(upload_file_name('img.jpg'))
    # browser.element('#uploadPicture')#.perform(upload_file_name('imgsss.jpg'))

    browser.element('#currentAddress').type(Student.address)

    #Прописать какой стейт и добавить переменные \ хелпер, смотреть скрин
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city').click()
    browser.element('#city #react-select-4-option-1').click()
    # browser.element('#uploadPicture').send_keys('/img.jpg')
    browser.element('#submit').perform(command.js.click)


    #Then
    def tr_table_search(number_tr):
        return browser.element(f'.table-responsive tbody tr:nth-child({number_tr}) td:nth-child(2)')

    tr_table_search(1).should(have.exact_text(f'{Student.name} {Student.lastname}'))
    tr_table_search(2).should(have.exact_text(Student.mail))
    tr_table_search(3).should(have.exact_text('Male'))
    tr_table_search(4).should(have.exact_text(Student.mobile_number))
    tr_table_search(5).should(have.exact_text(f'{Student.day} January,{Student.year}'))
    #Падает
    tr_table_search(6).should(have.exact_text(f'{Student.subjects[0]} {Student.subjects[1]}'))
    tr_table_search(7).should(have.exact_text(f'{Hobbies.music}, {Hobbies.sports}, {Hobbies.reading}'))
    tr_table_search(8).should(have.exact_text(f''))
    tr_table_search(9).should(have.exact_text(Student.address))
    tr_table_search(10).should(have.exact_text('Uttar Pradesh Lucknow'))

    import time
    time.sleep(5) #Для отладки