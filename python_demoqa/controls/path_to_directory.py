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

