"""{{cookiecutter.project_slug}}"""
import sys

from {{cookiecutter.project_slug}}.{{cookiecutter.project_slug}} import {{cookiecutter.project_slug}}
from PySide2.QtWidgets import QApplication

APP = QApplication([])
GUI = {{cookiecutter.project_slug}}()
GUI.show()
sys.exit(APP.exec_())
