# def File(filename, css_selector: Optional[str] = '#uploadPicture'):
#     browser.element(css_selector).send_keys(path_to_directory.filename(filename))

def filename(relative_path):
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

