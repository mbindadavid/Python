def say_hello():
    # block belonging to the function
    print('hello world')

    # end of function

say_hello() # call the function
#say_hello() # call the function again

# New function from here
def print_max(a, b):
    if a > b:
        print(a, 'is maximu')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

# Directly pass literal values
print_max(3, 4)

x = 5
y = 7

# pass variable as arguments
print_max(x,y)