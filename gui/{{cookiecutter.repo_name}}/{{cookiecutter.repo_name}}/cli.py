"""Console scripts for {{cookiecutter.repo_name}}."""
import sys

import click

from {{cookiecutter.repo_name}}.{{cookiecutter.repo_name}} import {{cookiecutter.repo_name}}
from PySide2.QtWidgets import QApplication


@click.group(
    invoke_without_command=True, context_settings=dict(help_option_names=["-h", "--help"]),
)
@click.pass_context
@click.version_option()
def cli(ctx):
    """{{cookiecutter.repo_name}}"""
    if ctx.invoked_subcommand is None:
        app = QApplication([])
        gui = {{cookiecutter.repo_name}}()
        gui.show()
        sys.exit(app.exec_())
