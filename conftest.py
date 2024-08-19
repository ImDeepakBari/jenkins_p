
import pytest

@pytest.fixture
def add_numbers():
    # Fixture to return a simple addition function
    def _add(a, b):
        return a + b
    return _add

@pytest.fixture
def multiply_numbers():
    # Fixture to return a simple multiplication function
    def _multiply(a, b):
        return a * b
    return _multiply
