# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description}}

## Installation

### Regular Install

1. `git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git`
2. `cd {{ cookiecutter.project_slug }}`
3. Create a virtual environment with `virtualenv .venv`
4. [Activate that environment](https://virtualenv.pypa.io/en/latest/)
5. `pip install .`

### Developer Install

1. `git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git`
2. `cd {{ cookiecutter.project_slug }}`
3. Create a virtual environment with `virtualenv .venv`
4. [Activate that environment](https://virtualenv.pypa.io/en/latest/)
5. `pip install -r requirements-dev.txt`
6. `pre-commit install`
7. `pip install -e .`
8. `tox`

## Usage

Usage Notes

## Developers Guide

Please see the [Contributing Guidelines](CONTRIBUTING.md).
