"""
Fibonacci iterator and generator
"""


class Fibonacci_seq():

    def __init__(self, n):

        self.max = n
        self.previous_number = 0
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.number == 0:
            self.number = 1
        else:
            self.previous_number, self.number = self.number, self.number + \
                                                            self.previous_number

        if self.previous_number > self.max:
            raise StopIteration

        return self.previous_number


def fib_generator(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b


if __name__ == "__main__":

    max = int(input("type a number\n"))
    fib = Fibonacci_seq(max)

    print("\nFibonacci iterator:")
    for i in fib:
        print(i, end=" ")

    print("\n\nFibonacci generator")
    fib_gen = fib_generator(max)

    for i in fib_gen:
        print(i, end=" ")
