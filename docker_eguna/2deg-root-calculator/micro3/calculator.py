import functools

def compute(a: float, b: float, c: float) -> list :

    x = [i for i in range(len(1000))]
    y = list(map(lambda x0: a * x * x + b * x + c, x))

    return x, y


