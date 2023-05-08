x = 50

def funct():
    global x

    print('x is', x)
    x = 2
    print('changed global x to', x)

funct()
print('value of x is', x) 
print('End of first function\n')   

# Define default value from here

def say(message, times=1):
    print(message * times)
    print('End of default value function\n')

say('Hello ') 
say('world ',5)   

# Function_keyword
def  func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
    print('End of fucntion keyword\n')

func(3, 7)
func(25, c=24)
func(c=50, a=100)

# VariArgs function
def total(a=5, *numbers, **phonebook):
    print('a', a)
    

    #Iterate through all item in turple
    for single_item in numbers:
        print('single_item', single_item)

    # Iterate through all item in dictionary
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)
        print('The end of varArgs fucntion\n')

total(10,1,2,3,Jack=1123,John=2231,Inge=1560) # Do not understand and make it clear

# Define return function
def maximum(x,y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'

    else:
        return y
print(maximum(2,3)) # What is the difference between print and return && why does this print not print if has indentation
print('The end of return function\n')

# Define fucntion docstring  from here (Dont understand what does it do clearly)

def print_max(x, y):
    '''Print the maximum of two possible.
    
    The two values must be intergers.'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__) # What is it doing exactly
