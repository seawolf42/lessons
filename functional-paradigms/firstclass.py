import functools

# "novice" way to do build a list of even numbers


def evens(start, stop):
    # evens(1, 11) => [2, 4, 6, 8, 10]
    result = []
    for i in range(start, stop):
        if i % 2 == 0:
            result.append(i)
    return result

# comprehensions-based


def evens_list_comprehension(start, stop):
    return [i * 2 for i in range(round(start / 2), stop // 2 + 1)]
    # or:  [i for i in range(start, stop) if i % 2 == 0]

# convert an iterable to a list


def evens_range_increment(start, stop):
    return list(range(start + start % 2, stop, 2))

# return a generator instead of a list


def evens_generator(start, stop):
    return range(start + start % 2, stop, 2)
    # or:  filter(lambda x: x % 2 == 0, range(start, stop))

# radical approach


def evens_generator_repeatable(start, stop):
    # gen_1_to_11 = evens_generator_repeatable(1, 11) <- returns a callable
    # list(gen_1_to_11()) => [2, 4, 6, 8 10] <- calling the callable
    return functools.partial(range, start + start % 2, stop, 2)
