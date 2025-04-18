.ONESHELL:

VENV = .venv
ROOT_DIR := $(shell poetry env info --path)
UNAME_S := $(shell uname -s)

# Determine OS and set paths accordingly.
ifeq ($(UNAME_S), Darwin)
    PYTHON = $(VENV)/bin/python
    PIP = $(VENV)/bin/pip
    BIN = $(VENV)/bin
    ACTIVATE = $(VENV)/bin/activate
else ifeq ($(UNAME_S), Linux)
    PYTHON = $(VENV)/bin/python
    PIP = $(VENV)/bin/pip
    BIN = $(VENV)/bin
    ACTIVATE = $(VENV)/bin/activate
else
    PYTHON = $(VENV)/Scripts/python
    PIP = $(VENV)/Scripts/pip
    BIN = $(VENV)/Scripts
    ACTIVATE = $(VENV)/Scripts/activate
endif


# Default target.
init: clean venv setup check-deps show-info activate


# Clean up files.
clean:
	rm -rf $(VENV) cdk.out build dist **/*.egg-info .pytest_cache node_modules .coverage .ruff_cache


# Create .venv from the pyproject.toml file.
venv:
	@echo "Definining the poetry configs..."
	poetry config --list | grep -q 'virtualenvs.in-project = true' || poetry config virtualenvs.in-project true

	@echo "Installing the dependencies..."
	poetry install --quiet


# Download the necessary libs.
setup:
	@echo "Install git"
	@if [ ! -d .git ]; then \
		echo "Initializing Git repository..."; \
		git init; \
	else \
		echo "Git already initialized."; \
	fi

	@echo "Install pre-commit"
	pre-commit clean
	pre-commit autoupdate
	pre-commit install

	@echo "Activate your venv, run: eval \$$(poetry env activate)"


# Check for required tools; fail fast if any are missing.
check-deps:
	@command -v poetry >/dev/null 2>&1 || { echo >&2 "❌ Poetry is not installed."; exit 1; }
	@command -v pre-commit >/dev/null 2>&1 || { echo >&2 "❌ pre-commit is not installed."; exit 1; }


# Run pytest with coverage.
test:
	@echo "Running tests with coverage..."
	@poetry run pytest --cov=tests/ --cov-report=term-missing --cov-report=html


# Show Python version and paths.
show-info:
	@echo "OS: $(UNAME_S)"
	@echo "Python path: $(PYTHON)"
	@echo "Pip path: $(PIP)"
	@echo "Bin directory: $(BIN)"
	@echo "Activate script: $(ACTIVATE)"
	@$(PYTHON) --version
	@poetry --version
	@poetry env info


# Target to remind how to activate the virtual environment.
activate:
	@echo "To activate the virtual environment, run:"
	@echo ""
	@echo "On Windows (CMD):"
	@echo "   source $(ACTIVATE)"
	@echo ""
	@echo "On Windows (PowerShell):"
	@echo "   & $(ACTIVATE)"
	@echo ""
	@echo "On Unix-like systems (Linux, macOS):"
	@echo "   eval \$$(poetry env activate)"


# Mark targets as phony.
.PHONY: init clean venv setup check-deps test show-info activate
