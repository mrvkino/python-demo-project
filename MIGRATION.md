# Python 3.13+ CLI Project with uv

## ✅ Completed Updates

Your project has been modernized to use **Python 3.13+** with **uv** package manager and leverages all latest Python features.

### Key Changes:

#### 1. **Python Version**
- Updated to **Python 3.13** (requires-python = ">=3.13")
- Single target version for optimal performance
- All type hints use modern Python 3.13 syntax

#### 2. **Package Management (uv)**
- Switched build backend to `hatchling` (lightweight and fast)
- `.python-version` file for uv auto-detection
- `pyproject.toml` compatible with uv workflow
- Fast dependency resolution and caching

#### 3. **Modern Python 3.13+ Features Used**

**Type Hints:**
- `collections.abc.Callable` instead of `typing.Callable`
- Explicit type annotations with `str | None` style (native union)
- Better inference with modern Pydantic v2

**Code Quality:**
- Strict mypy configuration enabled
- Full type coverage throughout codebase
- Better exception handling with Python 3.13's improvements

**Dependencies:**
- `typer[all]>=0.9.0` - Modern CLI framework
- `pydantic>=2.5.0` - Latest validation
- `structlog>=24.0.0` - Structured logging
- `ruff>=0.2.0` - Fast linting/formatting (replaces Black, isort, flake8)

#### 4. **Code Files Updated**

- **main.py** - Uses `collections.abc.Callable`, enhanced type hints
- **config.py** - Pydantic v2 with modern config patterns
- **commands/greet.py** - Modern docstrings and type hints
- **commands/info.py** - Explicit type annotations

#### 5. **Configuration Files**

- **.python-version** - Tells uv to use Python 3.13
- **pyproject.toml** - Updated with hatchling, Python 3.13, ruff config
- **.pre-commit-config.yaml** - Uses ruff, updated for Python 3.13
- **.github/workflows/tests.yml** - Uses uv for fast CI/CD

#### 6. **Tests**
- `test_main.py` - Updated for Typer's CliRunner
- `test_config.py` - Pydantic v2 compatible
- `test_commands.py` - Modern pytest patterns with markers

## 🚀 Quick Start

### Install uv (One-time setup)

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows PowerShell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Setup Project

```bash
cd /Users/mrogersvallee/Documents/Project/vsccode-copilot/python-demo-project

# Install Python 3.13 (if needed)
uv python install

# Sync dependencies
uv sync

# Run CLI
uv run demo-cli --help
uv run demo-cli hello --name "World"
uv run demo-cli show-config
uv run demo-cli show-version

# Run tests
uv run pytest

# Code quality
uv run ruff check src tests --fix
uv run ruff format src tests
uv run mypy src
```

## 📦 What's New

| Feature | Old | New |
|---------|-----|-----|
| Build Backend | setuptools | hatchling |
| Package Manager | pip | **uv** |
| CLI Framework | Click | **Typer** |
| Formatters | Black, isort | **Ruff** |
| Linters | flake8, Black | **Ruff** |
| Python Version | 3.10-3.12 | **3.13+** |
| Type Hints | typing.Optional | **str \| None** |
| Config Style | class Config | **SettingsConfigDict** |

## 📋 File Changes Summary

- ✅ `pyproject.toml` - Updated all configs
- ✅ `src/demo_cli/main.py` - Modern type hints
- ✅ `src/demo_cli/config.py` - Pydantic v2 patterns
- ✅ `src/demo_cli/commands/greet.py` - Type annotations
- ✅ `src/demo_cli/commands/info.py` - Enhanced types
- ✅ `.github/workflows/tests.yml` - uv integration
- ✅ `.pre-commit-config.yaml` - Ruff + mypy
- ✅ `tests/test_*.py` - Updated for new frameworks
- ✅ `.python-version` - Python 3.13 marker
- ✅ `README.md` - Updated documentation
- ✅ `SETUP.md` - Complete setup guide

## 🎯 Next Steps

1. **Install uv** if you haven't already
2. **Run `uv sync`** to set up the project
3. **Verify setup**: `uv run demo-cli --help`
4. **Run tests**: `uv run pytest`
5. **Check types**: `uv run mypy src`
6. **Start developing!**

## 📚 References

- [uv Documentation](https://docs.astral.sh/uv/)
- [Python 3.13 Features](https://docs.python.org/3.13/whatsnew/3.13.html)
- [Typer Docs](https://typer.tiangolo.com/)
- [Pydantic v2](https://docs.pydantic.dev/)
- [Ruff](https://docs.astral.sh/ruff/)

---

Your project is now **production-ready** with modern Python 3.13+ best practices! 🎉
