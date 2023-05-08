poem = '''\
David is a soldier
any soldier must follow an order
You cant be a soldier if you have disorder
'''

# open for 'w'riting
f = open('poem.txt', 'w')
# Write text to file
f.write(poem)
# Close the file
f.close()


# If no mode is specified
# 'r' ead mode is assume by default
f = open('poem.txt')
while True:
    line = f.readline()

# Zero lenght indicate of file
    if len(line) == 0:
       break
    # The `line` already has a newline
    # at the end of each line
    # since it is reading from a file.

    print(line,end='')

# Close the file
f.close()

