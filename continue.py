while True:
    s = input('Enter something : ')
    if s == 'quit':
        print('We are going to break this loop')
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')
    #Do anything here
    