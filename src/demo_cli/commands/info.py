"""Information commands.

Uses Python 3.14+ features like improved exception groups and
better type handling.
"""

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from demo_cli import __version__
from demo_cli.config import get_settings

console: Console = Console()


def show_config() -> None:
    """Display application configuration."""
    settings = get_settings()

    table: Table = Table(title="Application Configuration", show_header=True)
    table.add_column("Key", style="cyan")
    table.add_column("Value", style="magenta")

    for key, value in settings.model_dump().items():
        table.add_row(key, str(value))

    console.print(Panel(table, title="[bold]Config[/bold]"))


def show_version() -> None:
    """Display application version."""
    version_text = (
        f"[bold blue]Demo CLI[/bold blue] version "
        f"[bold green]{__version__}[/bold green]"
    )
    console.print(version_text)
    typer.echo("Built with modern Python best practices")
