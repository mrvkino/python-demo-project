"""Main CLI entry point.

Uses Python 3.14+ features including improved type hints and
stdlib improvements.
"""

import structlog
import typer
from rich.console import Console

from demo_cli.commands import async_cmd, greet, info

# Initialize logger
logger: structlog.typing.FilteringBoundLogger = structlog.get_logger()
console: Console = Console()

app: typer.Typer = typer.Typer(
    name="demo-cli",
    help="A modern Python CLI application with best practices",
    no_args_is_help=True,
    pretty_exceptions_enable=True,
)

# Register commands
app.command()(greet.hello)
app.command()(info.show_config)
app.command()(info.show_version)
app.command()(async_cmd.async_hello)


@app.callback()
def main(
    debug: bool = typer.Option(
        False,
        "--debug",
        help="Enable debug mode",
    ),
) -> None:
    """Initialize the application."""
    if debug:
        structlog.configure(
            processors=[
                structlog.processors.JSONRenderer(),
            ],
        )
        logger.debug("Debug mode enabled")


if __name__ == "__main__":
    app()
