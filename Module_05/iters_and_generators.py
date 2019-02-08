def _is_simple(number):

    i = 2

    divider = number // i

    while divider > 1:
        if (number % divider) == 0:
            return False
        else:
            i += 1
            divider = number // i

    return True

def get_params(integers=True):

    gen_range = int(input('Range?:\n'))
    if integers:
        inc = int(input('Increment?:\n'))
    else:
        inc = 0
    print('\n')

    return gen_range, inc

"""Iterator: From zero to given number with set increment"""
class IntNumbers:

    def __init__(self, _range, increment):
        self._range = _range
        self.increment = increment
        self.number = 0

    def __iter__(self):
        return self.number

    def __next__(self):
        number = self.number #to include zero at start
        self.number += self.increment
        if self.number > self._range:
            raise StopIteration

        return number


"""Generator: From zero to given number with set increment"""
def numbrs_generator(series_range, increment):

    return (x for x in range(0, series_range, increment))


"""Simple numbers iterator"""
class SNumbers:

    def __init__(self, _range, inc):
        """ Note param inc - to unify call with IntNumbers and numbrs_generator """
        self._range = _range
        self.number = -1

    def __iter__(self):
        return self.number

    def __next__(self):
        self.number += 1
        while not _is_simple(self.number):
            self.number += 1

        if self.number > self._range:
            raise StopIteration

        return self.number

"""Simple numbers generator """
def simple_nums_generator(series_range, inc):

    return (x for x in range(0, series_range) if _is_simple(x))


""" App """

print(
""" Please, select an option:
    1 - numbers iterator with increment;
    2 - numbers generator with increment;
    3 - simple number iterator;
    4 - simple number generator.
""")

series_container = [IntNumbers, numbrs_generator, SNumbers, simple_nums_generator]

try:
    choice = int(input(""))
    if choice < 5:
        if choice < 3:
            series_range, inc = get_params(True)
        else:
            series_range, inc = get_params(False)

        series = series_container[choice-1](series_range, inc)

        while True:
            try:
                print(next(series))
                s = input('Next>')
            except StopIteration:
                break
    else:
        print('Wrong choice. Please, restart.')

except ValueError:
    print('Wrong choice. Please, restart.')
