"""Tests for async CLI commands."""

from typer.testing import CliRunner

from demo_cli.main import app

runner = CliRunner()


def test_async_hello() -> None:
    """Test the async_hello command."""
    result = runner.invoke(app, ["async-hello", "--name", "AsyncWorld"])
    assert result.exit_code == 0
    assert "Hello AsyncWorld!" in result.output
    assert "asynchronously" in result.output.lower()
