"""{{ cookiecutter.project_slug }}"""
import logging

from PySide6 import QtCore, QtWidgets

from {{ cookiecutter.project_slug }}.qt_logger import QTLogHandler
from {{ cookiecutter.project_slug }}.view import console_colors
from {{ cookiecutter.project_slug }}.view.main_window import Ui_MainWindow

LOG = logging.getLogger("{{ cookiecutter.project_slug }}")


class Application(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # Override the qt designer outputs
        self.setWindowTitle("{{ cookiecutter.project_slug }}")
        self.statusbar.setVisible(False)
        self.stacked_widget.setCurrentIndex(0)

        self.connect_title_bar_buttons()
        self.connect_page_buttons()

        # Setup the logging infrastructure
        qt_log_handler = QTLogHandler()
        LOG.addHandler(qt_log_handler)
        qt_log_handler.new_record.connect(self.log_message)

    def connect_page_buttons(self) -> None:
        """Connect the buttons in the side bar to update which widget is shown."""
        self.log_btn.clicked.connect(
            lambda x: self.stacked_widget.setCurrentWidget(self.log_widget)
        )
        self.main_btn.clicked.connect(
            lambda x: self.stacked_widget.setCurrentWidget(self.main_widget)
        )
        self.settings_btn.clicked.connect(
            lambda x: self.stacked_widget.setCurrentWidget(self.settings_widget)
        )

    def connect_title_bar_buttons(self):
        """Connect the buttons in the title bar to actions."""
        self.minimize_btn.clicked.connect(lambda x: self.showMinimized())
        self.maximize_btn.clicked.connect(self.toggle_window_size)
        self.exit_btn.clicked.connect(lambda x: QtWidgets.QApplication.quit())

    def toggle_window_size(self) -> None:
        """Toggle between normal and maximized window size."""
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def log_message(self, level, msg) -> None:
        """Log any builtin logger messages to the log widget."""
        if level in console_colors.COLORS:
            self.log_textedit.appendHtml(
                f'<p style="color:{console_colors.COLORS[level]};">{msg}</p>'
            )
        else:
            self.log_textedit.appendPlainText(msg)
        self.log_textedit.ensureCursorVisible()
