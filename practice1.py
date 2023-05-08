def collatz(number):
    if number % 2 == 0:
       print(number //2)
    elif number % 2 == 1:
        print( 3 * number + 1)

    try:
       num1 = int(input("Please enter number: "))
       while num1 == collatz():
           if num1 == 1:
               break
    except:
        print("You must enter interger value")


collatz(3)



