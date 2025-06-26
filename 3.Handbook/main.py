class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"


roger = Dog("Roger")
print(roger.bark())  # Output: Roger says Woof!

rita = Dog("Rita")
print(rita.bark())  # Output: Rita says Woof!


def logtime(func):
    """Decorator to log the time taken by a function."""
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result

    return wrapper


@logtime
def slow_function():
    """Function that simulates a slow operation."""
    import time
    time.sleep(2)
    return "Finished slow function"


result = slow_function()  # Call the decorated function
print(result)  # Output: Finished slow function
