# Python Project Template

A comprehensive Python project template with modern tooling and best practices.

## 🚀 Quick Start

Create a new Python project from this template:

### Option 1: Using the Windows Setup Script
```cmd
setup_template.bat --output-dir my-new-project
```

### Option 2: Using Python Script Directly
```bash
python replace_template_vars.py --output-dir my-new-project
```

### Option 3: Manual Setup
1. Copy the `template/` directory contents to your desired location
2. Run the replacement script to customize template variables
3. Initialize as a new Git repository

## 📋 What You'll Get

The template creates a complete Python project with:

### 🏗️ **Modern Python Packaging**
- **Poetry** for dependency management and packaging
- **Namespace packages** support for organizations
- **pyproject.toml** configuration

### 🔧 **Development Tools**
- **pytest** for testing with comprehensive configuration
- **mypy** and **pyright** for static type checking
- **ruff** for fast linting and formatting
- **bandit** for security analysis
- **pre-commit hooks** for code quality

### 📚 **Documentation**
- **Sphinx** with automatic API documentation
- **Read the Docs** integration
- Example documentation structure

### 🔄 **CI/CD Pipeline**
- **GitHub Actions** workflows for:
  - Pull request validation
  - Multi-platform testing (Windows, Ubuntu, macOS)
  - Python 3.9-3.13 compatibility testing
  - Documentation building
  - PyPI publishing
- **Renovate** for dependency updates

### 🛡️ **Security & Quality**
- Security scanning with Bandit
- Dependency vulnerability checks
- Code coverage reporting
- CODEOWNERS file for repository governance

## 📝 Setup Process

When you run the setup script, you'll be prompted for:

- **Package name** (URL-friendly, short name)
- **Package namespace** (organization/company name)
- **Package display name** (human-readable name)
- **Package description**
- **Author and maintainer information**
- **Repository URLs**
- **Security contact email**
- **Code owner GitHub handles**

## 📁 Template Structure

```
template/
├── .github/           # GitHub Actions workflows and templates
├── docs/             # Sphinx documentation
├── examples/         # Usage examples
├── src/              # Source code with namespace structure
├── tests/            # Test suite with pytest configuration
├── .gitignore        # Python-specific gitignore
├── .readthedocs.yaml # Read the Docs configuration
├── pyproject.toml    # Poetry and tool configuration
├── LICENSE           # MIT License template
└── README.md         # Project README template
```

## � Detailed Usage Instructions

### Creating a New Project

1. **Run the setup script** (choose one method above)
2. **Follow the interactive prompts** to enter your project details:
   - Package name (e.g., `data-processor`)
   - Package namespace (e.g., `mycompany`)
   - Package display name (e.g., `My Data Processor`)
   - Package description
   - Author information
   - Repository URLs
   - Security contact
   - Code owners

3. **The script will:**
   - Copy all template files to your output directory
   - Replace all `{{template_variables}}` with your values
   - Rename namespace and package directories
   - Generate a ready-to-use Python project

### Example Usage

```cmd
# Windows
setup_template.bat --output-dir my-awesome-project

# Or cross-platform
python replace_template_vars.py --output-dir my-awesome-project
```

This creates a new directory `my-awesome-project/` with:
- Complete Python package structure
- Configured development tools
- GitHub Actions workflows
- Documentation setup
- Test framework

## �🔧 After Creating Your Project

1. **Navigate to your new project directory**
2. **Review and customize the generated files**
3. **Initialize Git repository:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit from template"
   ```
4. **Install dependencies:**
   ```bash
   poetry install --with dev,lint,test,docs
   ```
5. **Run tests to verify setup:**
   ```bash
   poetry run pytest
   ```
6. **Set up your GitHub repository and push code**

## 🤝 Contributing to This Template

This repository contains:
- `template/` - The actual template files
- `replace_template_vars.py` - Setup script for customizing templates
- `setup_template.bat` - Windows batch script wrapper
- `.github/` - Administration files for this template repository

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing improvements to this template.

## 📄 License

This template is released under the MIT License. Projects created from this template can use any license of your choice.