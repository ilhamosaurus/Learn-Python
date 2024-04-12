def luasPersegiPanjang(p, l):
    """
    Calculate the area of a rectangle given its length and width.

    Parameters:
    p (int): the length of the rectangle.
    l (int): the width of the rectangle.

    Returns:
    int: the calculated area of the rectangle.
    """
    luas = p * l
    return luas


persegiPertama = luasPersegiPanjang(10, 5)
print(persegiPertama)


def totalan(*args):
    """
    A function that calculates the total sum of the input arguments.

    Parameters:
    *args (tuple): Input arguments to be summed.

    Returns:
    int: The total sum of the input arguments.
    """
    print(type(args))
    total = sum(args)
    return total


print(totalan(1, 2, 3, 4, 5, 6, 7, 8, 9))


def info(**kwargs):
    """
    A function that generates a string representation of the key-value pairs in the provided **kwargs dictionary.
    This function takes in keyword arguments (**kwargs) and returns a string concatenating the keys and values.
    """
    print(type(kwargs))
    ingpo = ""
    for key, value in kwargs.items():
        ingpo += f"{key}: {value}\n"
    return ingpo


print(info(nama="Ilham", umur=27, hobi="Futsal"))


luasPersegi = lambda s: s**2  # lambda function
print(luasPersegi(5))


def minimal(a, b):
    if a <= b:
        return a
    else:
        return b


print(minimal(10, 7))


def greeting(name):
    print(f"Halo cak {name}")


greeting("ilham")
