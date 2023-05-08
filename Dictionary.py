# 'ab' is short for 'a'ddress'b'ook

ab = {
    'swaroop': 'swaroop@swarropch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer':'spammer@hotmail.com'
}

print("Swaroop`s address is", ab['swaroop'])

#Deleting a key value pair
del ab['Spammer']
print('\nThere are {} contacts on phonebook\n'.format(len(ab)))

for name, address in ab.items():
    print('contac {} at {}'.format(name, address))

#Adding a key value pair

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("Guido`s address is: ", ab['Guido'])

    ab['Name','Surname','Prof','Role'] = ['David','Mbinda','Coder','Soldier']
for key,value in ab.items():
    print('name {} in {} '.format(key,value))