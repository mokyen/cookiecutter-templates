.PHONY: clean test lint run

tox:
	tox

lint:
	tox -e flake8,pylint 

test:
	tox -e test

clean:
	rm -rf .tox .pytest_cache htmlcov *.egg-info .coverage