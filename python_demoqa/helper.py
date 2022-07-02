from pathlib import Path

print("File Path:", Path(__file__).parent.parent)

def upload_file_name(image):
    # v = Path().absolute()
    upload_path = Path(__file__)
    return f'{upload_path}/{image}'


# upload_file_name('img.jpg')
