# Python Project Template# {{package_display_name}}



A comprehensive Python project template with modern tooling and best practices.{{package_description}}



## Features## About



- **Modern Python packaging** with Poetry for dependency management`{{package_full_name}}` is the main Python package in this repo.

- **Code quality tools** with pre-commit hooks, mypy, ruff, and pytest

- **Documentation** with Sphinx and automatic API documentation{{author_name}} created and supports this package.

- **CI/CD** with GitHub Actions

- **Security** with safety checks and dependency scanning## Operating System Support

- **Development environment** with dev containers support

`{{package_full_name}}` supports Windows and Linux operating systems.

## Quick Start

## Python Version Support

### Option 1: Using the Setup Script (Windows)

`{{package_full_name}}` supports CPython 3.9+.

```cmd

setup_template.bat --output-dir my-new-project## Installation

```

You can directly install the `{{package_full_name}}` package using `pip` or by listing it as a

### Option 2: Using Python Script Directlydependency in your project's `pyproject.toml` file.



```bash```bash

python replace_template_vars.py --output-dir my-new-projectpip install {{package_full_name}}

``````



### Option 3: Manual SetupOr add to your `pyproject.toml`:



1. Copy the `template/` directory to your desired location```toml

2. Run the replacement script to customize the template variables[tool.poetry.dependencies]

3. Follow the setup instructions{{package_full_name}} = "^0.1.0"

```

## Template Structure

## Quick Start

The `template/` directory contains all the files that will be copied to your new project:

```python

- **Source code**: `src/` with namespace and package structureimport {{package_namespace}}.{{package_name}} as {{package_name}}

- **Tests**: `tests/` with pytest configuration

- **Documentation**: `docs/` with Sphinx setup# Add your quick start example here

- **Examples**: `examples/` with usage examples```

- **Configuration**: Poetry, mypy, ruff, and other tool configurations

- **CI/CD**: GitHub Actions workflows for testing and deployment## Documentation



## Template VariablesFull documentation is available at: {{documentation_url}}



When setting up a new project, you'll be prompted for:## Contributing



- Package name and namespaceSee [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

- Author and maintainer information

- Repository URLs## License

- Security contact information

- Code owner GitHub handlesThis project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Development

This repository contains:

- `template/` - The actual template files
- `replace_template_vars.py` - Setup script for customizing templates
- `setup_template.bat` - Windows batch script wrapper
- `.github/` - Administration files for this template repository

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to this template.

## License

This template is released under the MIT License. Projects created from this template can use any license.