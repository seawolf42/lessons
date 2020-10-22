import functools

NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# "novice" way to do build a list of even numbers

def evens(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result


evens(NUMBERS)  # => [2, 4, 6, 8]


def evens_list_comprehension(numbers):
    return [number for number in numbers if number % 2 == 0]


def evens_generator(numbers):
    return (number for number in numbers if number % 2 == 0)


def evens_filter(numbers):
    return filter(lambda x: x % 2 == 0, numbers)


def evens_repeatable(numbers):
    return functools.partial(evens_generator, numbers)


evens_again = evens_repeatable(NUMBERS)  # <- returns a callable
list(evens_again())  # => [2, 4, 6, 8] # <- calling the callable
list(evens_again())  # => [2, 4, 6, 8] # <- calling it again


