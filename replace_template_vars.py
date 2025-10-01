#!/usr/bin/env python3
"""Script to replace template variables with actual values."""

import argparse
import os
import re
import shutil
from pathlib import Path
from typing import Dict


def get_template_variables() -> Dict[str, str]:
    """Get template variables from user input."""
    print("Python Template Variable Replacement")
    print("====================================")
    print()
    
    variables = {}
    
    # Required variables
    variables['package_name'] = input("Package name (short, URL-friendly): ").strip()
    variables['package_namespace'] = input("Package namespace (e.g., company name): ").strip()
    variables['package_full_name'] = f"{variables['package_namespace']}.{variables['package_name']}"
    variables['package_display_name'] = input("Package display name (human-readable): ").strip()
    variables['package_description'] = input("Package description: ").strip()
    variables['author_name'] = input("Author name: ").strip()
    variables['author_email'] = input("Author email: ").strip()
    variables['maintainer_name'] = input("Maintainer name: ").strip()
    variables['maintainer_email'] = input("Maintainer email: ").strip()
    
    # Repository info
    repo_owner = input("GitHub username/organization: ").strip()
    repo_name = f"{variables['package_name']}-python"
    variables['repository_url'] = f"https://github.com/{repo_owner}/{repo_name}"
    variables['documentation_url'] = f"https://{repo_name}.readthedocs.io"
    
    # Security and ownership
    variables['security_email'] = input("Security contact email: ").strip()
    variables['code_owner_handle'] = input("Code owner GitHub handle (with @): ").strip()
    variables['code_owner_handle_2'] = input("Second code owner GitHub handle (with @, optional): ").strip()
    
    return variables


def replace_in_file(file_path: Path, variables: Dict[str, str]) -> None:
    """Replace template variables in a file."""
    try:
        content = file_path.read_text(encoding='utf-8')
        
        for var_name, var_value in variables.items():
            if var_value:  # Only replace if value is not empty
                content = content.replace(f'{{{{{var_name}}}}}', var_value)
        
        file_path.write_text(content, encoding='utf-8')
        print(f"Updated: {file_path}")
    except Exception as e:
        print(f"Error updating {file_path}: {e}")


# CODEOWNERS handling is no longer needed - template has the correct file structure


def rename_directories(base_path: Path, variables: Dict[str, str]) -> None:
    """Rename directories that contain template variables."""
    # Rename source directories
    src_path = base_path / "src"
    if src_path.exists():
        # Rename namespace directory
        old_namespace_path = src_path / "{{package_namespace}}"
        if old_namespace_path.exists():
            new_namespace_path = src_path / variables['package_namespace']
            old_namespace_path.rename(new_namespace_path)
            print(f"Renamed: {old_namespace_path} -> {new_namespace_path}")
            
            # Rename package directory
            old_package_path = new_namespace_path / "{{package_name}}"
            if old_package_path.exists():
                new_package_path = new_namespace_path / variables['package_name']
                old_package_path.rename(new_package_path)
                print(f"Renamed: {old_package_path} -> {new_package_path}")


def main() -> int:
    """Main function."""
    parser = argparse.ArgumentParser(description="Replace template variables")
    parser.add_argument("--template-dir", default="template", help="Template directory path")
    parser.add_argument("--output-dir", help="Output directory (default: current directory)")
    parser.add_argument("--config", help="Config file with variable values")
    
    args = parser.parse_args()
    
    template_dir = Path(args.template_dir).resolve()
    output_dir = Path(args.output_dir or ".").resolve()
    
    if not template_dir.exists():
        print(f"Error: Template directory {template_dir} does not exist")
        return 1
    
    # Always copy template to output directory
    if template_dir == output_dir:
        print(f"Error: Cannot use template directory {template_dir} as output directory")
        return 1
    
    if output_dir.exists() and any(output_dir.iterdir()):
        print(f"Error: Output directory {output_dir} already exists and is not empty")
        return 1
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy template contents to output directory
    for item in template_dir.iterdir():
        if item.is_dir():
            shutil.copytree(item, output_dir / item.name)
        else:
            shutil.copy2(item, output_dir / item.name)
    print(f"Copied template to: {output_dir}")
    
    # Get variables
    if args.config:
        # TODO: Implement config file loading
        print("Config file loading not yet implemented")
        return 1
    else:
        variables = get_template_variables()
    
    print("\nReplacing template variables...")
    
    # File extensions to process
    extensions = {'.py', '.md', '.yml', '.yaml', '.toml', '.rst', '.txt', '.json'}
    
    # Process all files
    for file_path in output_dir.rglob('*'):
        if file_path.is_file() and file_path.suffix in extensions:
            # Skip binary files and special directories
            if any(part.startswith('.git') for part in file_path.parts):
                continue
                
            replace_in_file(file_path, variables)
    
    # Rename directories
    print("\nRenaming directories...")
    rename_directories(output_dir, variables)
    
    # CODEOWNERS handling is no longer needed - template has the correct file structure
    
    print("\nTemplate replacement complete!")
    print(f"Project created in: {output_dir}")
    print("\nNext steps:")
    print("1. Review the generated files")
    print("2. Initialize git repository: git init")
    print("3. Install dependencies: poetry install --with dev,lint,test,docs")
    print("4. Run tests: poetry run pytest")
    print("5. Set up your GitHub repository")
    
    return 0


if __name__ == "__main__":
    exit(main())