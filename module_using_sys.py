import sys

print('The command line arguments are:\n')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

# Not understand what is sys doing and the output is differ from mine.

# Module use name start from here

if __name__ == '__main__':
    print('This is being run by it self\n\n')

else:
    print('I have been imported from other module\n\n')
    # Not understand this module how its works

    # Create my own module from here

def say_hi():
    print('This is my module speaking..\n')

def love():
    print('I love python\n')

__version__ = '1.0'

# calling my won module from here which is the same file

import module_using_sys
module_using_sys.say_hi()
module_using_sys.love()
print('version', module_using_sys.__version__)