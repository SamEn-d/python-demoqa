from typing import Optional

from selene.support.shared import browser

from python_demoqa.controls import path_to_directory

def File(filename, css_selector: Optional[str] = '#uploadPicture'):
    browser.element(css_selector).send_keys(path_to_directory.filename(filename))
    ...

# browser.element('#uploadPicture').send_keys(path_to_directory.filename('img.jpg'))