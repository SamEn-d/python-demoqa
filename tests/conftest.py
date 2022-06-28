from selene.support.shared import browser
import pytest

@pytest.fixture(scope='function', autouse=True)
def base_url():
    browser.config.base_url = ('https://demoqa.com/')
    '''
    #Размер окна, не сделан здесь, для большей возможности использования и дальнейшей проверки на мобилках
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    '''
    '''
    #альтернативный вариант
    browser.driver.set_window_size(width=1920, height=1080)
    '''