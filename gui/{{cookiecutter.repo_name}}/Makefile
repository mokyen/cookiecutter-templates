.PHONY: gui clean test lint run

gui:
	pyside2-uic ./{{cookiecutter.repo_name}}/gui.ui -o ./{{cookiecutter.repo_name}}/gui.py

tox:
	tox -p all

lint:
	tox -e flake8,pylint 

test:
	tox -e test

clean:
	rm -rf .tox .pytest_cache htmlcov *.egg-info .coverage