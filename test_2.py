def add(x, y):
    return x + y

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def concat(a, b):
    return a + b

def test_concat():
    assert concat("Hello, ", "World!") == "Hello, World!"
    assert concat("", "empty") == "empty"

def is_even(num):
    return num % 2 == 0

def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False


def list_length(lst):
    return len(lst)

def test_list_length():
    assert list_length([1, 2, 3]) == 3
    assert list_length([]) == 0


def maximum(x, y):
    return x if x > y else y

def test_maximum():
    assert maximum(10, 20) == 20
    assert maximum(30, 25) == 30

def to_uppercase(s):
    return s.upper()

def test_to_uppercase():
    assert to_uppercase("hello") == "HELLO"
    assert to_uppercase("WORLD") == "WORLD"

def multiply(x, y):
    return x * y

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0


def contains(lst, item):
    return item in lst

def test_contains():
    assert contains([1, 2, 3], 2) is True
    assert contains([1, 2, 3], 4) is False

def square(x):
    return x * x

def test_square():
    assert square(3) == 9
    assert square(-4) == 16

def is_substring(s, sub):
    return sub in s

def test_is_substring():
    assert is_substring("hello world", "world") is True
    assert is_substring("hello world", "earth") is False
