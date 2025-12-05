"""Greeting commands.

Demonstrates modern Python 3.14 CLI patterns with type hints.
"""

import typer
from rich.console import Console

console: Console = Console()


def hello(
    name: str = typer.Option(
        ...,
        "--name",
        "-n",
        help="Name to greet",
    ),
) -> None:
    """Greet someone with a friendly message.

    Example:
        demo-cli hello --name "World"
    """
    console.print(f"[bold green]Hello {name}![/bold green]")
    console.print("[dim]Welcome to Demo CLI[/dim]")
