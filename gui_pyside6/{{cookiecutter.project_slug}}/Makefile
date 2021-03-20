.PHONY: view clean

view:
	PySide6-uic ./{{ cookiecutter.project_slug }}/view/main_window.ui -o ./{{ cookiecutter.project_slug }}/view/main_window.py --from-imports
	PySide6-rcc ./{{ cookiecutter.project_slug }}/view/icons.qrc -o ./{{ cookiecutter.project_slug }}/view/icons_rc.py

clean:
	rm -rf .tox .pytest_cache htmlcov *.egg-info .coverage
