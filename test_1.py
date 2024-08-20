# test_operations.py
def test_addition(add_numbers):
    result = add_numbers(3, 5)
    assert result == 8, f"Expected 8 but got {result}"

def test_addition_negative(add_numbers):
    result = add_numbers(6, 5)
    assert result == 9, f"Expected 11 but got {result}"

def test_multiplication(multiply_numbers):
    result = multiply_numbers(3, 5)
    assert result == 15, f"Expected 15 but got {result}"

def test_multiplication_negative(multiply_numbers):
    result = multiply_numbers(7, 5)
    assert result == 15, f"Expected 35 but got {result}"

def test_assert():
    assert True
