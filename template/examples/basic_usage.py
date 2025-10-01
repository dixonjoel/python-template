"""Example usage of {{package_display_name}}."""

# This is a placeholder example file.
# Replace this with actual examples showing how to use your package.

from {{package_namespace}}.{{package_name}}.example import ExampleClass, example_function


def main():
    """Demonstrate basic usage of the package."""
    # Example 1: Using the example function
    result = example_function(5, 10)
    print(f"5 + 10 = {result}")
    
    # Example 2: Using the example class
    obj = ExampleClass("Hello, World!")
    print(f"Stored value: {obj.get_value()}")
    
    # Change the value
    obj.set_value("New value")
    print(f"Updated value: {obj.get_value()}")


if __name__ == "__main__":
    main()