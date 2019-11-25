"""{{cookiecutter.repo_name}}"""
import sys

from {{cookiecutter.repo_name}}.{{cookiecutter.repo_name}} import {{cookiecutter.repo_name}}
from PySide2.QtWidgets import QApplication

APP = QApplication([])
GUI = {{cookiecutter.repo_name}}()
GUI.show()
sys.exit(APP.exec_())
