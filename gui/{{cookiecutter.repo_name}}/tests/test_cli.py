"""
Tests for `cli` module.
"""
from click.testing import CliRunner

import pytest
from {{cookiecutter.repo_name}} import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.cli, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message and exit." in help_result.output
