def decarator_sub(func):
    def wrapper(n1, n2):
        if n1 < n2:
            (n1, n2) = (n2, n1)
        return func(n1, n2)

    return wrapper


@decarator_sub
def sub(n1, n2):
    return n1 - n2


print(sub(6, 5))
