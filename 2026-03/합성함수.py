def add_three(x):
    return x+3

def square(x):
    return x*x

compose_function = lambda x: square(add_three(x))
print(compose_function(3))