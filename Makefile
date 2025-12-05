UV := uv

# Make `ci-checks` the default target so `make` runs the full CI sequence.
.DEFAULT_GOAL := ci-checks

.PHONY: help sync lint format-check type-check test ci-checks

help:
	@echo "Makefile targets:"
	@echo "  make sync          # create/update venv and install all deps (all extras)"
	@echo "  make lint          # run ruff check"
	@echo "  make format-check  # run ruff format --check"
	@echo "  make type-check    # run mypy"
	@echo "  make test          # run pytest"
	@echo "  make ci-checks     # run all of the above in sequence"

sync:
	$(UV) sync --all-extras

lint:
	$(UV) run ruff check src tests

format-check:
	$(UV) run ruff format --check src tests

type-check:
	$(UV) run mypy src

test:
	$(UV) run pytest --verbose

ci-checks: sync lint format-check type-check test
