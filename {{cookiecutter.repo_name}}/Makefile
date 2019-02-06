.PHONY: clean test lint run

tox:
	tox -p all

lint:
	tox -e flake8,pylint 

test:
	tox -e test

clean:
	rm -rf .tox .pytest_cache htmlcov *.egg-info .coverage