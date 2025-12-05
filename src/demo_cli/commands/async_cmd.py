"""Async commands demonstrating modern async support in Python 3.14."""

import asyncio

import typer
from rich.console import Console

console: Console = Console()


async def _async_greet(name: str) -> str:
    # simulate an async I/O operation
    await asyncio.sleep(0.01)
    return f"Hello {name}!"


def async_hello(
    name: str = typer.Option(
        ...,
        "--name",
        "-n",
        help="Name to greet asynchronously",
    ),
) -> None:
    """Greet someone using an async helper but expose a sync command.

    The wrapper runs the async helper via ``asyncio.run`` so Typer's
    sync runner (CliRunner) and normal command-line use work without
    leaving unpaid coroutines.
    """
    # Run the async helper in a new event loop
    greeting = asyncio.run(_async_greet(name))
    console.print(f"[bold green]{greeting}[/bold green]")
    console.print("[dim]This greeting was produced asynchronously.[/dim]")
