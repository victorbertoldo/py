def teste(x, y, z=None, *args):
    if(z is None):
        return x + y
    else:
        return x + y + z


print(teste(1, 2))

print(teste(1, 2, 3))
