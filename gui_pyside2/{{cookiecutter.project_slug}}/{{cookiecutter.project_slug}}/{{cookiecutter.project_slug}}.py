"""{{cookiecutter.project_slug}}"""
from {{ cookiecutter.project_slug }} import logger
from {{ cookiecutter.project_slug }}.gui import Ui_MainWindow

from PySide2 import QtCore, QtWidgets

CONSOLE_TEXT_COLORS = {
    "WARNING": "black",
    "INFO": "black",
    "DEBUG": "darkCyan",
    "CRITICAL": "red",
    "ERROR": "red",
}

class {{cookiecutter.project_slug}}(QtWidgets.QMainWindow, Ui_MainWindow)):

    def __init__(self, verbose=False):
        self.log = logger.setup_logger("{{ cookiecutter.project_slug }}", "{{ cookiecutter.project_slug }}.log")

        if verbose:
            self.log.setLevel(logging.DEBUG)
        else:
            self.log.setLevel(logging.INFO)

        self.setupUi(self)

        # Setup the rest of the GUI.
        self.setWindowTitle("{{ cookiecutter.project_slug }}")
        self.connect_actions()
        self.console_dock.setVisible(True)
        self.menubar.setNativeMenuBar(False)  # Until Qt fixes QMenu for Catalina

        # Add another handler so that we can emit log messages to the GUI.
        thread_log = ThreadLogHandler()
        self.log.addHandler(thread_log)
        thread_log.new_record.connect(self.log_message)
   
    def connect_actions(self) -> None:
        """Connect all the GUI elements to the business logic."""
        self.actionExit.triggered.connect(quit_app)

    def log_message(self, level, msg) -> None:
        """Log any logger messages via the slot/signal mechanism so that its thread safe."""
        if level in CONSOLE_TEXT_COLORS:
            self.console.appendHtml(f'<p style="color:{CONSOLE_TEXT_COLORS[level]};">{msg}</p>')
        else:
            self.console.appendPlainText(msg)
        self.console.ensureCursorVisible()


def quit_app() -> None:
    """Quit the application."""
    QtCore.QCoreApplication.instance().quit()