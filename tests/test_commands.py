"""Tests for the greeting commands."""

import pytest
from typer.testing import CliRunner

from demo_cli.main import app

runner = CliRunner()


@pytest.mark.unit
class TestGreetCommand:
    """Test greeting commands."""

    def test_hello_with_name(self) -> None:
        """Test hello command with name."""
        result = runner.invoke(app, ["hello", "--name", "Bob"])
        assert result.exit_code == 0
        assert "Hello Bob!" in result.output

    def test_hello_required_name(self) -> None:
        """Test hello command without name fails."""
        result = runner.invoke(app, ["hello"])
        assert result.exit_code != 0
