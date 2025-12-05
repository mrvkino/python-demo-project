"""Tests for the main CLI module."""

import pytest
from typer.testing import CliRunner

from demo_cli.main import app

runner = CliRunner()


@pytest.mark.unit
def test_cli_hello() -> None:
    """Test the hello command."""
    result = runner.invoke(app, ["hello", "--name", "World"])
    assert result.exit_code == 0
    assert "Hello World!" in result.output
    assert "Welcome to Demo CLI" in result.output


@pytest.mark.unit
def test_cli_hello_with_short_option() -> None:
    """Test the hello command with short option."""
    result = runner.invoke(app, ["hello", "-n", "Alice"])
    assert result.exit_code == 0
    assert "Hello Alice!" in result.output


@pytest.mark.unit
def test_cli_config() -> None:
    """Test the config command."""
    result = runner.invoke(app, ["show-config"])
    assert result.exit_code == 0
    assert "Configuration" in result.output


@pytest.mark.unit
def test_cli_version() -> None:
    """Test the version command."""
    result = runner.invoke(app, ["show-version"])
    assert result.exit_code == 0
    assert "Demo CLI" in result.output
    assert "version" in result.output.lower()


@pytest.mark.unit
def test_cli_help() -> None:
    """Test the help command."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "modern Python CLI" in result.output
