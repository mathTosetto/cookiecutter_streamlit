# Python Template with Cookiecutter

This is a Python template generated with Cookiecutter.

## Prerequisites
Before you begin, ensure you have the following installed:
- `pip install py-make`
- `pip install cookiecutter`

## Getting Started
To get started with this template, follow these steps:

1. Download the template:
   ```bash
   cookiecutter <repository_url>
   ```

2. Execute the Makefile:
   ```bash
   make init # or pymake init
   ```

3. Activate the .venv:
   ```bash
   source .venv/Scripts/activate # Windows
   eval $(poetry env activate) # OS
   ```

Rename .env.template:
   ```bash
   cp .env.template .env
   rm .env.template
   ```