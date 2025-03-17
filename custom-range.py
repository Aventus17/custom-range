def my_range(stop: int, start: int = 0, step: int = 1) -> list:
    if type(stop) == int and type(start) == int and type(step) == int:
        if step == 0:
            raise ValueError("my_range() arg 3 must not be zero.")
        elif step > 0:
            result = []

            i = start

            while i < stop:
                result.append(i)
                i += step

            return result
        else:
            result = []

            i = start

            while i > stop:
                result.append(i)
                i += step

            return result
    else:
        raise ValueError("An invalid value was entered.")


# print(list(range(5, 30, -2)))
# print(my_range(30, 5, -2))

# print(list(range(50, 30, -2)))
# print(my_range(30, 50, -2))

# print(list(range(55, 20, 2)))
# print(my_range(20, 55, 2))

# print(list(range(5, 20, 2)))
# print(my_range(20, 5, 2))

# print(list(range(20, 5, 5)))
# print(my_range(20, 5, -1))

# print(list(range(5, 20, 0)))
# print(my_range(20, 5, 0))

# print(list(range(20, 5)))
# print(my_range(5, 20))

# print(list(range('olma')))
# print(my_range('olma'))

# print(list(range(-10)))
# print(my_range(-10))

# print(list(range(10)))
# print(my_range(10))

# print(list(range(5, 20)))
# print(my_range(20, 5))

# print(list(range(5, 30, 2)))
# print(my_range(30, 5, 2))
