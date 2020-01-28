# Contributing Guidelines
Thank you for taking an interest in `{{ cookiecutter.project_slug }}`!  We are happy to accept PRs for any fixes.  If you
are wanting to add a new feature, submit an issue first so that we can talk about it.  You are more
than welcomed to go ahead and start on that feature on your fork and link it to the issue.

## Getting Starting

Fork the repo and follow the instructions for installing and setting up `{{ cookiecutter.project_slug }}` in the [README](README.md).  You will need to replace the URL with the URL for your forked repo.  This installation process should run you through the whole flow.

## Code Style/Formating

Black is used for formatting the code base.  There is a `pyproject.toml` file that should set it to
the correct line length and any other settings.  You can run the formatter in one of three ways:

- `black .` from the root directory, which will format everything.
- `tox -e format` from the root directory, which will cleanup the import order and then
black format the code.
- Just commit as normal!  If you ran `pre-commit install` during installation that installed black as
a pre-commit hook and it should run every time you commit.

## Testing

Tox is used as the test runner for local development.  From the root directory, running `tox -p all`
will run all environments in parallel but make the output harder to digest.  You can run them serially
by just running `tox`.  If one is failing use `tox -e {ENV_THAT_IS_FAILING}` to just run the one.

Before submitting a PR, these should all be passing.
