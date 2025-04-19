# Python Template with Cookiecutter

This is a Python template generated with Cookiecutter.

---

## Getting Started

Run `make` from Makefile for available commands:
   ```bash
   make
   ```

Rename .env.template:
   ```bash
   cp .env.template .env
   rm .env.template
   ```

Enable logging:
   ```python
   # Add this snippet to your script
   import logging

   LOGGER: logging.Logger = logging.getLogger("your_module_or_app_name")
   ```
