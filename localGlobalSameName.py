def spam():
    eggs = 'spam local'
    print(eggs) # Print 'spam local'

def bacon():
    eggs = 'bacom local'
    print(eggs) # print 'bacon local'
    spam()
    print(eggs)  # print 'bacon local'

eggs = 'global'
bacon()
print(eggs)  # print 'global'

