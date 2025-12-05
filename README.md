# Demo CLI

A modern Python CLI application built with best practices and Python 3.14+ features.

## Features

- Clean architecture with separation of concerns
- Type hints with strict mypy checking
- Configuration management with Pydantic
- Rich terminal output
- Comprehensive testing with pytest
- CI/CD ready with GitHub Actions
- Modern dependency management with `uv`
- Uses latest Python 3.13+ features

## Installation

### Prerequisites

- Python 3.13 or higher
- `uv` package manager (recommended)

### From source with uv

```bash
git clone <repository-url>
cd demo-cli
uv sync
```

### With pip

```bash
git clone <repository-url>
cd demo-cli
pip install -e ".[dev]"
```

## Usage

```bash
demo-cli --help
demo-cli hello --name "World"
demo-cli show-config
demo-cli show-version
```

## Development

### Setup with uv

```bash
# uv automatically creates virtual environment
uv sync
uv run demo-cli --help
```

### Running tests

```bash
uv run pytest
```

### Code quality with uv

```bash
# Format code
uv run ruff format src tests

# Lint
uv run ruff check src tests --fix

# Type checking
uv run mypy src
```

### Pre-commit hooks

```bash
uv run pre-commit install
```

## Project Structure

```
demo-cli/
├── src/demo_cli/          # Main package
│   ├── __init__.py
│   ├── main.py            # CLI entry point
│   ├── config.py          # Configuration with Pydantic
│   ├── commands/          # Command modules
│   │   ├── greet.py
│   │   └── info.py
│   └── py.typed           # PEP 561 marker
├── tests/                 # Test suite with pytest
├── docs/                  # Documentation
├── pyproject.toml         # Project metadata with uv
├── README.md              # This file
└── .python-version        # Python version for uv
```

## Technology Stack

- **Python 3.14+** - Latest Python features
- **Typer** - Modern CLI framework with type hints
- **Pydantic v2** - Data validation and settings
- **Rich** - Beautiful terminal output
- **Structlog** - Structured logging
- **Ruff** - Fast Python linter and formatter
- **Pytest** - Testing framework
- **uv** - Fast Python package manager

## Python 3.14 Features Used

- Enhanced type hints with `collections.abc`
- Improved exception groups
- Better type inference
- Streamlined error messages

## License

MIT License - see LICENSE file for details
