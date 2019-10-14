""" {{cookiecutter.repo_name}} """
import logging
import platform
import sys
from pathlib import Path

from {{cookiecutter.repo_name}} import __version__ as VERSION
from {{cookiecutter.repo_name}}.logger import ThreadLogHandler, setup_logger
from {{cookiecutter.repo_name}}.view.gui import {{cookiecutter.repo_name}}_GUI
from PySide2.QtCore import QCoreApplication, QThread
from PySide2.QtWidgets import QApplication


class {{cookiecutter.repo_name}}:

    def __init__(self):
        self.log = setup_logger("{{cookiecutter.repo_name}}", Path(__file__).parent.joinpath("{{cookiecutter.repo_name}}.log"))

        app = QApplication([])
        self.gui = {{cookiecutter.repo_name}}_GUI()

        thread_log = ThreadLogHandler()
        thread_log.new_record.connect(self.gui.log_message)
        self.log.addHandler(thread_log)

        self.gui.show()

        self.log.info(
            "System: %s %s Version: %s", platform.system(), platform.release(), platform.version()
        )
        self.log.info("Python Version: %s", platform.python_version())
        self.log.info("{{cookiecutter.repo_name}} Version: %s", VERSION)
        self.log.info("Starting {{cookiecutter.repo_name}}...")


        # Slot/Signal Connections between the GUI and {{cookiecutter.repo_name}}
        # ----------------------------------------------------------------------------------------
        app.aboutToQuit.connect(self.close_application)

        sys.exit(app.exec_())

    def close_application(self):
        """Close any threads and then kill the application."""
        QCoreApplication.instance().quit()

    def toggle_debug_mode(self, state):
        """Turn on or off debug throughout {{cookiecutter.repo_name}}."""
        if state:
            self.log.setLevel(logging.DEBUG)
        else:
            self.log.setLevel(logging.INFO)


def main():
    {{cookiecutter.repo_name}}()


if __name__ == "__main__":
    main()
