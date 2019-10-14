import logging
import logging.handlers
import platform

from PySide2.QtCore import QObject, Signal


def setup_logger(root_name, log_file_path):
    """Setup the File Handler.  All messages are logged."""
    log = logging.getLogger(root_name)
    file_handler = logging.handlers.RotatingFileHandler(
        log_file_path, maxBytes=10485760, backupCount=5  # 10MB
    )
    fh_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(fh_format)
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)

    log.setLevel(logging.DEBUG)

    log.info("Log file created at: %s", log_file_path)
    return log


class LogQObject(QObject):
    """Create a dummy object to get around the PySide multiple inheritance problem."""

    new_record = Signal(str, str)

    def __init__(self):
        super().__init__()


class ThreadLogHandler(logging.Handler):
    """Create a custom logging handler that appends each record to the TextEdit Widget."""

    def __init__(self):
        super().__init__()
        self.log = LogQObject()
        self.new_record = self.log.new_record
        self.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        self.setLevel(logging.DEBUG)

    def emit(self, record):
        """Let the GUI know there is a new message."""
        msg = self.format(record)
        level = record.levelname
        self.new_record.emit(level, msg)
