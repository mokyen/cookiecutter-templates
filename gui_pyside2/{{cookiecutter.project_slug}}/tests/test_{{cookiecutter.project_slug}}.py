import pytest

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}


@pytest.fixture
def window(qtbot):
    """Pass the application to the test functions via a pytest fixture."""
    new_window = {{cookiecutter.project_slug }}.{{cookiecutter.project_slug }}()
    qtbot.add_widget(new_window)
    new_window.show()
    return new_window


def test_window_title(window):
    """Check that the window title shows as declared."""
    assert window.windowTitle() == '{{ cookiecutter.project_slug }}'
