def test_bake_project(cookies):
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == "django-base-capybaday"
    assert result.project.isdir()
