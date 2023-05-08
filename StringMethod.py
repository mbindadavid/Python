# string

name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes,the string start with "Swa"')

if 'a' in name:
    print('Yes, string contain "a"')

if name.find('war') != -1:
    print('Yes,string contains "war"')
else:
    print('Correct place')

delimiter = '__*__'
mystring = ['Brazil','Russia','Tanzania','Arusha']

print(delimiter.join(mystring))