"""Command Line Interface for {{cookiecutter.project_slug}}"""
import sys
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'click' %}
from {{cookiecutter.project_slug}} import {{cookiecutter.project_slug}}
from PySide2.QtWidgets import QApplication

@click.group(
    invoke_without_command=True, context_settings=dict(help_option_names=["-h", "--help"])
)
@click.pass_context
@click.option("--verbose", "-vv", is_flag=True, help="Enable debug prints.")
@click.version_option()
def cli(ctx, verbose):
    """CLI for {{cookiecutter.project_slug}}"""
    ctx.obj = verbose
    click.echo("Opening {{cookiecutter.project_slug}} GUI.")
    if ctx.invoked_subcommand is None:
        app = QApplication([])
        gui = {{cookiecutter.project_slug}}.{{cookiecutter.project_name}}(verbose)
        gui.show()
        sys.exit(app.exec_())

@cli.command()
def sub_command_one():
    """Example Sub Command"""
    click.echo("{{cookiecutter.project_slug}} sub_command_one")
{%- endif %}
