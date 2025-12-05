# Setup Guide for Python 3.14+ with uv

This project uses **uv**, the blazing fast Python package installer, and requires **Python 3.14** or higher.

## Installing uv

### macOS (Recommended)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Linux/WSL

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

See [uv installation docs](https://docs.astral.sh/uv/getting-started/installation/) for more options.

## Installing Python 3.14

uv can manage Python versions automatically:

```bash
uv python install 3.14
```

Or use your system package manager:

- **macOS**: `brew install python@3.14`
- **Ubuntu/Debian**: `sudo apt-get install python3.14 python3.14-venv`
- **Fedora**: `sudo dnf install python3.14`
- **Windows**: Download from [python.org](https://www.python.org/)

## Project Setup

### Quick Start

```bash
cd /path/to/demo-cli
uv sync              # Install all dependencies
uv run demo-cli --help
```

### Development Workflow

```bash
# Activate the virtual environment (optional)
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate  # Windows

# Run CLI
uv run demo-cli hello --name "World"

# Run tests
uv run pytest

# Code quality checks
uv run ruff check src tests --fix
uv run ruff format src tests
uv run mypy src

# Pre-commit hooks
uv run pre-commit install
```

## Why uv?

- **Lightning fast**: 10-100x faster than pip
- **Single tool**: Replaces pip, pip-tools, and venv
- **Familiar**: Works like pip with familiar commands
- **Reliable**: Deterministic installs with lockfile
- **Modern**: Built with Python 3.14+ in mind

## Python 3.14 Features in This Project

This project leverages Python 3.14 features:

- **PEP 696**: Type parameter defaults
- **PEP 701**: Syntactic formalization of f-strings
- **PEP 688**: Making the buffer protocol accessible in Python
- Enhanced type hints with `collections.abc`
- Improved error messages and exception groups
- Better performance and stdlib improvements

## Project Structure

```bash
demo-cli/
├── .python-version         # uv reads this for Python version
├── pyproject.toml          # Project metadata with uv config
├── uv.lock                 # Lockfile for reproducible installs
├── src/
│   └── demo_cli/           # Main package
├── tests/                  # Test suite
└── docs/                   # Documentation
```

## Troubleshooting

### Python 3.14 not found

```bash
# Let uv install Python 3.14
uv python install 3.14

# Or check current Python
python --version
```

### Clear cache and reinstall

```bash
uv cache clean
uv sync --refresh
```

### Virtual environment issues

```bash
# Remove and recreate
rm -rf .venv
uv sync
```

For more help, see [uv documentation](https://docs.astral.sh/uv/).
