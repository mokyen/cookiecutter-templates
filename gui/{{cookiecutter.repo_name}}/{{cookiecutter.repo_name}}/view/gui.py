""" {{cookiecutter.repo_name}} """

import logging
import platform
import webbrowser

from {{cookiecutter.repo_name}} import __version__ as VERSION
from {{cookiecutter.repo_name}}.view.ui import Ui_MainWindow
from PySide2.QtCore import *
from PySide2.QtWidgets import *

TEXT_COLOR = {
    "WARNING": "black",
    "INFO": "black",
    "DEBUG": "navy",
    "CRITICAL": "red",
    "ERROR": "red",
}


class {{cookiecutter.repo_name}}_GUI(QMainWindow, Ui_MainWindow):
    """Main {{cookiecutter.repo_name}} Window"""

    def __init__(self):
        QMainWindow.__init__(self)
        self.log = logging.getLogger("{{cookiecutter.repo_name}}.gui")
        self.log.debug("Initializing GUI")
        self.setupUi(self)
        self.setWindowTitle("{{cookiecutter.repo_name}}")
        self.create_statusbar()
        self.connect_actions()
        self.console.setVisible(False)
        self.showMaximized()

    def connect_actions(self):
        self.actionE_xit.triggered.connect(QCoreApplication.instance().quit)
        self.actionAbout.triggered.connect(self.about)
        self.actionDocumentation.triggered.connect(open_docs)

    def create_statusbar(self):
        """Create a bar across the bottom for messages."""
        self.status_label = QLabel()
        self.statusBar().addPermanentWidget(self.status_label)

    def log_message(self, level, msg):
        """Log any logger messages via the slot/signal mechanism so that its thread safe."""
        self.text_edit.ensureCursorVisible()
        if level in TEXT_COLOR:
            self.text_edit.appendHtml(f'<p style="color:{TEXT_COLOR[level]};">{msg}</p>')
        else:
            self.text_edit.appendPlainText(msg)

    @Slot(str)
    def update_statusbar(self, status_str):
        """Update the content of the status bar."""
        self.status_label.setText(status_str)

    def about(self):
        """Popup a Message Box with the About information."""
        QMessageBox.about(
            self,
            self.tr(f"{{cookiecutter.repo_name}} v{VERSION}"),
        )


def open_docs():
    """Open the documentation."""
    webbrowser.open("https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}")
