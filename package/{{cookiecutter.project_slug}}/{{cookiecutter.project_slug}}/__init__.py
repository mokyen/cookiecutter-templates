__author__ = '{{ cookiecutter.full_name }}'
__version__ = '{{ cookiecutter.version }}'

{% if cookiecutter.application_library|lower == 'library' %}
import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())
{%- endif %}