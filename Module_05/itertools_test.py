import itertools
import operator


def simple_func():
    """ Simple function """
    return 5

def _count():
    """ Count. counts to 10 """
    a = itertools.count(1, step=1)
    b = 0
    c = []
    while b < 10:
        c.append(a.__next__())
        b += 1
    return c


def _cycle():
    """ Cycles 'Баба Яга' 5 times """

    a = 0
    b = itertools.cycle(['Баба', 'Яга'])
    c = []
    while a < 10:
        c.append(b.__next__())
        a += 1

    return c

def _repeat():
    """ Repeat """

    return list(itertools.repeat('Баба Яга', 3))

def _accumulate():
    """ Accumulate """
    return list(itertools.accumulate((1,2,3,4,5), operator.add))

def discount():
    """ Discounts Investment by rate for n equal periods """

    I = int(input("Investment?"))
    r = float(input("rate?")) / 100
    n = int(input("periods?"))
    cash_flow = [I/n for x in range(n-1)]
    cash_flow.insert(0, -I)

    discounted_cash_flow = list(itertools.accumulate(
                                cash_flow, lambda bal, pmt: bal / (1 + r) + pmt))

    return cash_flow, discounted_cash_flow

def logistic_map():
    """ Logistic Map """

    log_map = lambda x, r: r * x * (1 - x)
    r = 0.5
    x0 = 1.0
    inputs = itertools.repeat(x0, 20)
    return [format(x, '.2f') for x in itertools.accumulate(inputs, log_map)]

def _compress():
    """ Compress """
    return 'Баба Яга', ''.join(itertools.compress(
                                                'Баба Яга', [1,1,1,1,0,1,1,0]))

iter_list = [simple_func, _count, _cycle, _repeat, _accumulate, discount,
            logistic_map, _compress]

if __name__ == "__main__":
    for number, item in list(enumerate(iter_list)):
        print(number, item.__doc__)
    choice = int(input("Enter sequence to generate:\n"))

    func_to_run = iter_list[choice]
    print(func_to_run())
