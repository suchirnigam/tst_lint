import os  # Unused import

def some_function():  # Missing docstring
    x = 5
    if x > 3:
        y = "Bye"
        print(y)
    return x

def MyFunction():  # Invalid function name (Pylint prefers snake_case)
    pass

class MyClass:  # Missing docstring
    def __init__(self):
        self.val = 10

    def add(self, a, b):
        return a + b

def some_long_function_name_that_is_too_complex_to_read():
    for i in range(100):
        if i % 2 == 0:
            print(i)
        else:
            for j in range(50):
                if j % 5 == 0:
                    print(i * j)
    return i
