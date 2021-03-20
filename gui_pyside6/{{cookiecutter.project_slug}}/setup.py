from setuptools import find_packages, setup


def readme():
    """Open up the readme and use the text for the long description."""
    with open("README.md") as f:
        return f.read()


setup(
    name="{{ cookiecutter.project_slug }}",
    version="{{ cookiecutter.version }}",
    author="{{ cookiecutter.full_name }}",
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme(),
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    packages=find_packages(),
    install_requires=[
        "Pyside6",
    ],
    python_requires=">=3.8",
)
