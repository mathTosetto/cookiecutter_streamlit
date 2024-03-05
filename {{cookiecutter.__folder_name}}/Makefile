.ONESHELL:

VENV = .venv
PIP = $(VENV)/Scripts/pip
PYTHON = $(VENV)/Scripts/python
BIN = $(VENV)/Scripts
UV = $(VENV)/Scripts/uv

# Default target
init:
    clean
    venv
    setup_dependencies

# Clean up files
clean:
    rm -rf $(VENV) cdk.out build dist **/*.egg-info .pytest_cache node_modules .coverage

# Create .venv
venv:
    python -m venv $(VENV)

# Download the necessary libs
setup_dependencies:
    $(PYTHON) -m pip install --upgrade pip
    $(PIP) install uv
    $(UV) pip install -r requirements.txt

# Mark targets as phony
.PHONY:
    init
    clean
    venv
    setup_dependencies
