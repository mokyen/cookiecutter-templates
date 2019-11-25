""" {{cookiecutter.repo_name}}"""
import json
import platform
import webbrowser
from pathlib import Path

from {{cookiecutter.repo_name}} import __author__, __version__
from {{cookiecutter.repo_name}}.gui import Ui_MainWindow
from {{cookiecutter.repo_name}}.logger import ThreadLogHandler, setup_logger
from PySide2 import QtCore, QtWidgets

CONSOLE_TEXT_COLORS = {
    "WARNING": "black",
    "INFO": "black",
    "DEBUG": "darkCyan",
    "CRITICAL": "red",
    "ERROR": "red",
}


class {{cookiecutter.repo_name}}(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main {{cookiecutter.repo_name}} Window"""

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.log = setup_logger("{{cookiecutter.repo_name}}", Path(__file__).parent.joinpath("{{cookiecutter.repo_name}}.log"))

        self.setupUi(self)

        # Setup the rest of the GUI.
        self.setWindowTitle("{{cookiecutter.repo_name}}")
        self.connect_actions()
        self.console_dock.setVisible(True)
        self.menubar.setNativeMenuBar(False)  # Until Qt fixes QMenu for Catalina

        # Add another handler so that we can emit log messages to the GUI.
        thread_log = ThreadLogHandler()
        self.log.addHandler(thread_log)
        thread_log.new_record.connect(self.log_message)

        # Record the system information.
        self.log_system_information()

        # Initialize Variables for Prototype
        self.project_file = None
        self._configuration = {"version": __version__}

        # self.read_in_config("example.json")

    def connect_actions(self):
        """Connect all the GUI elements to the business logic."""
        # Global App Controls
        self.actionExit.triggered.connect(QtCore.QCoreApplication.instance().quit)
        self.actionAbout.triggered.connect(self.about)
        self.actionDocumentation.triggered.connect(documentation)


    def log_system_information(self):
        """Log the system information to aid in debugging user issues."""
        self.log.info(f"System: {platform.system()} {platform.release()}")
        self.log.info(f"Python Version: {platform.python_version()}")
        self.log.info(f"{{cookiecutter.repo_name}} Version: {__version__}")

    def log_message(self, level, msg):
        """Log any logger messages via the slot/signal mechanism so that its thread safe."""
        if level in CONSOLE_TEXT_COLORS:
            self.console.appendHtml(f'<p style="color:{CONSOLE_TEXT_COLORS[level]};">{msg}</p>')
        else:
            self.console.appendPlainText(msg)
        self.console.ensureCursorVisible()

    def about(self):
        """Pop-up MessageBox with Generic Info."""
        QtWidgets.QMessageBox.about(
            self,
            self.tr(f"{{cookiecutter.repo_name}} v{__version__}"),
            self.tr(
                f"{{cookiecutter.project_short_description}}"
                f"Version: {__version__}\n"
                f"Authors: {__author__}\n"
            ),
        )


def documentation():
    """Open the documentation for {{cookiecutter.repo_name}}."""
    webbrowser.open("https://github.com/jdpatt/{{cookiecutter.repo_name}}")
