import logging
import sys

from PySide6.QtWidgets import QApplication

from {{ cookiecutter.project_slug }} import __version__
from {{ cookiecutter.project_slug }}.application import Application


def main():
    """Main Entry Point."""

    LOG = logging.getLogger("{{ cookiecutter.project_slug }}")
    LOG.setLevel(logging.DEBUG)

    Q_APP = QApplication([])
    APP = Application()

    LOG.info("Application Version: v{}".format(__version__))
    APP.show()

    sys.exit(Q_APP.exec_())


if __name__ == "__main__":
    main()
