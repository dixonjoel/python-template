# Python Template

This is a template for creating Python packages with modern tooling and best practices.

## Using This Template

1. **Copy the template directory** to your new project location
2. **Replace template variables** with your project-specific values
3. **Initialize git repository** and make your first commit
4. **Set up development environment**

## Template Variables

The following template variables need to be replaced throughout the codebase:

### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{package_name}}` | Short package name (used in URLs, filenames) | `datastore` |
| `{{package_namespace}}` | Python namespace (often company/org name) | `ni` |
| `{{package_full_name}}` | Full package name for PyPI | `ni.datastore` |
| `{{package_display_name}}` | Human-readable package name | `NI Data Store` |
| `{{package_description}}` | Brief description of the package | `APIs for publishing and retrieving data` |
| `{{author_name}}` | Author/organization name | `NI` |
| `{{author_email}}` | Contact email for the author | `opensource@ni.com` |
| `{{maintainer_name}}` | Primary maintainer name | `John Doe` |
| `{{maintainer_email}}` | Maintainer contact email | `john.doe@company.com` |
| `{{repository_url}}` | GitHub repository URL | `https://github.com/ni/datastore-python` |
| `{{documentation_url}}` | Documentation URL | `https://datastore-python.readthedocs.io` |
| `{{security_email}}` | Security contact email | `security@company.com` |
| `{{code_owner_handle}}` | GitHub handle for code owner | `@johndoe` |
| `{{code_owner_handle_2}}` | Second GitHub handle for code owner | `@janedoe` |

### How to Replace Variables

#### Method 1: Search and Replace (Recommended)

Use your IDE's search and replace functionality to replace all instances:

1. Search for: `{{package_name}}`
2. Replace with: `your-package-name`
3. Repeat for all variables above

#### Method 2: Script-based Replacement

Create a script to automate the replacement:

```bash
#!/bin/bash
# replace_template_vars.sh

# Define your values
PACKAGE_NAME="mypackage"
PACKAGE_NAMESPACE="mycompany"
PACKAGE_FULL_NAME="mycompany.mypackage"
PACKAGE_DISPLAY_NAME="My Package"
PACKAGE_DESCRIPTION="A great Python package"
AUTHOR_NAME="My Company"
AUTHOR_EMAIL="info@mycompany.com"
MAINTAINER_NAME="John Doe"
MAINTAINER_EMAIL="john.doe@mycompany.com"
REPOSITORY_URL="https://github.com/mycompany/mypackage-python"
DOCUMENTATION_URL="https://mypackage-python.readthedocs.io"
SECURITY_EMAIL="security@mycompany.com"
CODE_OWNER_HANDLE="@johndoe"
CODE_OWNER_HANDLE_2="@janedoe"

# Replace in all files
find . -type f -name "*.py" -o -name "*.md" -o -name "*.yml" -o -name "*.toml" -o -name "*.rst" | \
xargs sed -i "s/{{package_name}}/$PACKAGE_NAME/g"
# ... repeat for all variables
```

### Renaming Files and Directories

After replacing template variables, you'll need to rename files and directories:

1. Rename `src/{{package_namespace}}` to `src/your-namespace`
2. Rename `src/your-namespace/{{package_name}}` to `src/your-namespace/your-package`
3. Rename `.github/workflows/check_{{package_name}}.yml` to `.github/workflows/check_your-package.yml`

## Post-Template Setup

### 1. Initialize Git Repository

```bash
git init
git add .
git commit -m "Initial commit from template"
```

### 2. Set Up Development Environment

```bash
# Install Poetry if not already installed
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install --with dev,lint,test,docs

# Activate virtual environment
poetry shell
```

### 3. Verify Setup

```bash
# Run tests
poetry run pytest

# Run linting
poetry run ni-python-styleguide lint

# Build documentation
cd docs && poetry run sphinx-build -b html . _build/html
```

### 4. GitHub Setup

1. Create a new repository on GitHub
2. Add the remote origin:
   ```bash
   git remote add origin https://github.com/yourusername/yourpackage-python.git
   git push -u origin main
   ```
3. Set up branch protection rules
4. Configure GitHub Actions secrets if needed
5. Set up code owners for the repository

### 5. Documentation Setup

1. Create account on [Read the Docs](https://readthedocs.org/)
2. Import your GitHub repository
3. Configure build settings using the included `.readthedocs.yaml`

### 6. PyPI Setup

1. Create account on [PyPI](https://pypi.org/)
2. Set up PyPI API token
3. Add the token as a GitHub secret named `PYPI_API_TOKEN`

## What's Included

### Project Structure
- Modern Python package structure with namespace support
- Comprehensive test suite with pytest
- Documentation with Sphinx and Read the Docs integration
- Example code and usage patterns

### Development Tools
- **Poetry**: Dependency management and packaging
- **Black**: Code formatting
- **MyPy**: Static type checking
- **PyRight**: Additional type checking
- **Bandit**: Security analysis
- **ni-python-styleguide**: Comprehensive linting

### CI/CD Pipeline
- GitHub Actions workflows for:
  - Pull request validation
  - Continuous integration
  - Documentation building
  - PyPI publishing
- Multi-platform testing (Windows, Ubuntu, macOS)
- Multiple Python version support (3.9-3.13)

### Documentation
- Sphinx-based documentation
- AutoAPI for automatic API documentation
- Read the Docs configuration
- Example documentation structure

### Quality Assurance
- Comprehensive test configuration
- Code coverage reporting
- Security scanning
- Dependency update automation with Renovate

## Customization Tips

### Adding Dependencies

Add to `pyproject.toml`:
```toml
[tool.poetry.dependencies]
requests = "^2.28.0"
```

### Adding Development Tools

Add to the appropriate group in `pyproject.toml`:
```toml
[tool.poetry.group.dev.dependencies]
your-dev-tool = "^1.0.0"
```

### Modifying CI/CD

Edit the workflow files in `.github/workflows/` to customize:
- Python versions to test
- Operating systems to support
- Additional quality checks
- Deployment strategies

### Documentation Customization

- Modify `docs/conf.py` for Sphinx configuration
- Add content to `docs/` directory
- Customize the theme and styling

## Best Practices

1. **Version Management**: Use semantic versioning (semver.org)
2. **Commit Messages**: Follow conventional commits
3. **Documentation**: Keep README and docs up to date
4. **Testing**: Maintain high test coverage
5. **Security**: Regularly update dependencies
6. **Licensing**: Review and update LICENSE as needed

## Getting Help

If you encounter issues with this template:

1. Check the existing documentation
2. Review similar projects for examples
3. Consult the tool-specific documentation:
   - [Poetry](https://python-poetry.org/docs/)
   - [Sphinx](https://www.sphinx-doc.org/)
   - [pytest](https://docs.pytest.org/)
   - [GitHub Actions](https://docs.github.com/en/actions)

## Contributing to the Template

If you have improvements for this template, please consider contributing back to help others benefit from your enhancements.