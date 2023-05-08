number = 23
guess = float(input('Enter a value '))
#What if I want to enter any data type and code should change it automatical into int or float
#guess = input('Enter a value '.format)
if guess == number:
    #new block start here
    print('congratulation,you guess it!')
    print('(but you do not win any prize!!)')
    #new block end here
elif guess < number:
    #another block start here
    print('No, it is little higher than that')
    #You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have a guessed > number to reach here

print('Done')
#This last statement is executed after if the statement is executed
 