# OOP Simple

'''class Person:
    #pass # an empty block

p = Person()
print(p)

# 
    def say_hi(self): # what if self removed? why is it not excute
     print('Hello,how are you!')

p = Person()
p.say_hi() '''

# Intiate

class Person:
    def __int__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello,my name is', self.name) 

p = Person('Swaroop')
p.say_hi()
#Person('Mbinda').say_hi()

