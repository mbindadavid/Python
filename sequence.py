# List, turpes and strings are examples of sequence
shoplist = ['aple','mango','carrot','banana']
name = 'swaroop'

#Indexing or 'subscription' operation #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

#Slicing on a list #
print('\nItem 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[0:])

# Slicing on string #
print('\nCharacter 1 to 3 is', name[1:3])
print('Character 2 to end is', name[2:])
print('Character 1 to -1 is', name[1:-1])
print('Character start to end is', name[0:])
print('\nSlicing for given values is', shoplist[::-2]) #Not printing correct values

