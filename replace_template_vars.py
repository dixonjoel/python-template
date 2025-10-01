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


def handle_codeowners_file(base_path: Path) -> None:
    """Handle CODEOWNERS file transformation."""
    github_path = base_path / ".github"
    if not github_path.exists():
        return
    
    codeowners_path = github_path / "CODEOWNERS"
    codeowners_template_path = github_path / "CODEOWNERS_TEMPLATE"
    
    # Remove existing CODEOWNERS (if it exists)
    if codeowners_path.exists():
        codeowners_path.unlink()
        print(f"Removed: {codeowners_path}")
    
    # Rename CODEOWNERS_TEMPLATE to CODEOWNERS
    if codeowners_template_path.exists():
        codeowners_template_path.rename(codeowners_path)
        print(f"Renamed: {codeowners_template_path} -> {codeowners_path}")


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
    
    # Rename workflow file
    workflow_path = base_path / ".github" / "workflows"
    if workflow_path.exists():
        old_workflow = workflow_path / "check_{{package_name}}.yml"
        if old_workflow.exists():
            new_workflow = workflow_path / f"check_{variables['package_name']}.yml"
            old_workflow.rename(new_workflow)
            print(f"Renamed: {old_workflow} -> {new_workflow}")


def main() -> int:
    """Main function."""
    parser = argparse.ArgumentParser(description="Replace template variables")
    parser.add_argument("--template-dir", default=".", help="Template directory path")
    parser.add_argument("--output-dir", help="Output directory (default: template-dir)")
    parser.add_argument("--config", help="Config file with variable values")
    
    args = parser.parse_args()
    
    template_dir = Path(args.template_dir).resolve()
    output_dir = Path(args.output_dir or args.template_dir).resolve()
    
    if not template_dir.exists():
        print(f"Error: Template directory {template_dir} does not exist")
        return 1
    
    # Copy template to output directory if different
    if template_dir != output_dir:
        if output_dir.exists():
            print(f"Error: Output directory {output_dir} already exists")
            return 1
        shutil.copytree(template_dir, output_dir)
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
            if file_path.name == 'replace_template_vars.py':
                continue
                
            replace_in_file(file_path, variables)
    
    # Rename directories
    print("\nRenaming directories...")
    rename_directories(output_dir, variables)
    
    # Handle CODEOWNERS file transformation
    print("\nHandling CODEOWNERS files...")
    handle_codeowners_file(output_dir)
    
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