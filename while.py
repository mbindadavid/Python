number = 28
running = True

while running:
    guess = float(input('Enter a number.. '))
    if number == guess:
        print('Congratulation,you got it!')
        #This cause the running to stop
        running = False

    elif guess < number:
        print('No,its a bit higher than that')
    else:
        print('No,its a bit lower than that')

else:
        print('The while loop is over')
#Do any magic here
print('By '*3)
