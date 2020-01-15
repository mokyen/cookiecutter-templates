from setuptools import setup

def readme():
    """Open up the readme and use the text for the long description."""
    with open("README.md") as f:
        return f.read()


setup(
    name="{{ cookiecutter.project_slug }}",
    version="0.1.0",
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme(),
    author="{{ cookiecutter.full_name }}",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main',
        ],
    },
    {%- endif %}
    packages=[
        "{{ cookiecutter.project_slug }}",
    ],
    package_dir={"{{ cookiecutter.project_slug }}": "{{ cookiecutter.project_slug }}"},
    include_package_data=True,
    install_requires=[
    ],
    license="MIT",
    zip_safe=False,
    keywords="{{ cookiecutter.project_slug }}",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
