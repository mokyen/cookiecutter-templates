"""The logging and debug functionality for prototype"""
import logging

from PySide2.QtCore import QObject, Signal


def setup_logger(root_name, log_file_path=""):
    """Setup the Handlers and set the default level to DEBUG."""
    log = logging.getLogger(root_name)

    # Setup a Console Logger
    console_handler = logging.StreamHandler()
    ch_format = logging.Formatter("%(message)s")
    console_handler.setFormatter(ch_format)
    console_handler.setLevel(logging.ERROR)
    log.addHandler(console_handler)

    # Setup a File Logger
    file_handler = logging.FileHandler(log_file_path, mode="w", delay=True)
    fh_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(fh_format)
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)

    log.setLevel(logging.DEBUG)

    log.info(f"Log file created at: {log_file_path}")
    return log


class LogQObject(QObject):
    """Create a dummy object to get around the PySide multiple inheritance problem."""

    new_record = Signal(str, str)


class ThreadLogHandler(logging.Handler):
    """Create a custom logging handler that appends each record to the TextEdit Widget."""

    def __init__(self):
        super().__init__()
        self.log = LogQObject()
        self.new_record = self.log.new_record
        self.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
        self.setLevel(logging.INFO)

    def emit(self, record):
        """Append the record to the Widget.  Color according to 'TEXT_COLOR'."""
        msg = self.format(record)
        level = record.levelname
        self.new_record.emit(level, msg)
