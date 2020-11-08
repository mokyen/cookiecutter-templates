"""Logging Handler interface to QT's signal/slot system."""
import logging

from PySide2.QtCore import QObject, Signal


class LogQObject(QObject):
    """Create a dummy object to get around the PySide multiple inheritance problem."""

    new_record = Signal(str, str)


class QTLogHandler(logging.Handler):
    """A Log Handler that uses QT's signal/slot system."""

    def __init__(self):
        super().__init__()
        self.log = LogQObject()
        self.new_record = self.log.new_record
        self.setFormatter(
            logging.Formatter(
                "%(asctime)s - %(levelname)s - %(name)s -  %(message)s", "%d%b%Y %H:%M:%S"
            )
        )
        self.setLevel(logging.INFO)

    def emit(self, record):
        """Emit a new record with the level before the message."""
        msg = self.format(record)
        level = record.levelname
        self.new_record.emit(level, msg)
