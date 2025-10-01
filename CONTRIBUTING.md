# Contributing to Python Project Template

Thank you for your interest in contributing to this Python project template!

## Types of Contributions

### Template Improvements
- Adding new features or tools to the template structure
- Updating dependencies and configurations
- Improving documentation and examples
- Enhancing CI/CD workflows

### Setup Script Enhancements
- Improving the `replace_template_vars.py` script
- Adding new template variables
- Better error handling and user experience
- Cross-platform compatibility improvements

### Documentation
- Improving the README and usage instructions
- Adding examples and tutorials
- Documenting best practices

## Development Process

1. **Fork and Clone**: Fork this repository and clone your fork locally
2. **Create Branch**: Create a feature branch for your changes
3. **Make Changes**: 
   - For template changes: modify files in the `template/` directory
   - For script changes: modify `replace_template_vars.py` or `setup_template.bat`
4. **Test**: Test your changes by creating a new project from the template
5. **Submit PR**: Submit a pull request with a clear description of your changes

## Testing Your Changes

To test template changes:

```bash
# Create a test project
python replace_template_vars.py --output-dir test-project

# Verify the generated project works
cd test-project
poetry install --with dev,lint,test,docs
poetry run pytest
```

## Template Structure Guidelines

- Keep the `template/` directory focused on project template files
- Administrative files should stay in the root directory
- Use template variables (e.g., `{{package_name}}`) for customizable content
- Follow Python packaging best practices
- Maintain compatibility with modern Python versions (3.9+)

## Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names and comments
- Test your changes thoroughly

## Questions?

Feel free to open an issue if you have questions about contributing!