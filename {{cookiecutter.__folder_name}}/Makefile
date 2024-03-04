.PHONY: venv

# Default target
venv: .venv/bin/activate

.venv/bin/activate: requirements.txt
    @echo "Creating virtual environment..."
    @rm -rf .venv
    @python3 -m venv .venv
    @. .venv/bin/activate; \
    pip install --upgrade pip setuptools wheel; \
    pip install uv; \
    uv pip install -r requirements.txt
