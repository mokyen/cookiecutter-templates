"""Command Line Interface for {{cookiecutter.project_slug}}"""
import sys
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.group(
    invoke_without_command=True, context_settings=dict(help_option_names=["-h", "--help"])
)
@click.pass_context
@click.version_option()
def main(ctx):
    """CLI for {{cookiecutter.project_slug}}"""
    click.echo("{{cookiecutter.project_slug}}")

@cli.command()
def sub_command_one():
    """Example Sub Command"""
    click.echo("{{cookiecutter.project_slug}} sub_command_one")
{%- endif %}

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
