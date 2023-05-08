import time, sys
indent = 0 # How many space to indent
indentIncreasing = True # Whether the indentation is increasing or not

try:
    while True: #The main program loop.
        print(' ', * indent, end='') # TypeError: Value after * must be an iterable, not int 
        print('********')
        time.sleep(0.1) # Pause for 1/10 of second.

        if indentIncreasing:
            # Increasing the number of spaces:
            indent = indent + 1
            if indent == 20:
                # change direction:
                indentIncreasing = False
        else:
            # Decreasing the number of spaces:
            indent = indent - 1
            if indent == 0:
                #change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
