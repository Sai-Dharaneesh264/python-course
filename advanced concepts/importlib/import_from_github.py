
def main(a, b):

    if b == 0:
        raise ZeroDivisionError('cannot divide')

    return a / b

print(main(4, 2))
print(main(4, 0))