class SchoolMember:
    '''Represent any school member'''
    def __int__(self,name,age): #What does __init__ do ????
        self.name = name
        self.age = age
        print('(Initializing schoolMember: {})'.format(self.name))

    def tell(self):
        '''Tell my details'''
        print('Name: "{}" Age: "{}"'.format(self.name, self.age), end='')


class Teacher(SchoolMember):
    '''Represent a teacher'''
    def __init__(self, name, age,salary):
        SchoolMember.__init__(self,name, age)
        self.salary = salary
        print('(Initialized Tacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{d}"'.format(self.salary))

class Student(SchoolMember):
    '''Represent student'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: {}'.format(self.marks))

t = Teacher('Major Mbinda', 40, 5000000) 
s = Student('2Lt David', 30, 95)

# Print a blank line

print()

members = [t, s]
for member in members:
    # Works for both teacher and student
    member.tell()


