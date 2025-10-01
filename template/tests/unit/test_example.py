"""Unit tests for the example module."""

import pytest

from {{package_namespace}}.{{package_name}}.example import ExampleClass, example_function


class TestExampleClass:
    """Test cases for ExampleClass."""

    def test_init_default(self):
        """Test ExampleClass initialization with default value."""
        obj = ExampleClass()
        assert obj.get_value() is None

    def test_init_with_value(self):
        """Test ExampleClass initialization with a value."""
        test_value = "test"
        obj = ExampleClass(test_value)
        assert obj.get_value() == test_value

    def test_set_and_get_value(self):
        """Test setting and getting values."""
        obj = ExampleClass()
        test_value = 42
        obj.set_value(test_value)
        assert obj.get_value() == test_value

    def test_value_overwrite(self):
        """Test overwriting existing values."""
        obj = ExampleClass("initial")
        obj.set_value("new_value")
        assert obj.get_value() == "new_value"


class TestExampleFunction:
    """Test cases for example_function."""

    def test_positive_numbers(self):
        """Test example_function with positive numbers."""
        result = example_function(2, 3)
        assert result == 5

    def test_negative_numbers(self):
        """Test example_function with negative numbers."""
        result = example_function(-2, -3)
        assert result == -5

    def test_mixed_numbers(self):
        """Test example_function with mixed positive and negative numbers."""
        result = example_function(-2, 5)
        assert result == 3

    def test_zero_values(self):
        """Test example_function with zero values."""
        result = example_function(0, 0)
        assert result == 0

    @pytest.mark.parametrize("x,y,expected", [
        (1, 1, 2),
        (10, 20, 30),
        (-5, 5, 0),
        (100, -50, 50),
    ])
    def test_parametrized_addition(self, x, y, expected):
        """Test example_function with various parameter combinations."""
        result = example_function(x, y)
        assert result == expected