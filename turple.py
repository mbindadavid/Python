''' I would recommend always using parentheses
to indicate start and end of tuple
 even though parentheses are optional.
Explicit is better than implicit.'''

zoo = ('python','elephant','penguine')
print('Number of animals in the zoo is:', len(zoo))

new_zoo = 'camel', 'monkey',zoo # paranthes are not neccessary but are recommended
print('Number of cages in the new zoo are', len(new_zoo))
print('all animals in the new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animal in the new zoo is:', len(new_zoo)-1 + len(new_zoo[2]))


