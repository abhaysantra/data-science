# https://www.youtube.com/watch?v=jCzT9XFZ5bw

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property 	# using property decorator we can use class method as class attribute.
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email) 	# here email is instance method not attribute but able to access as attribute because of @property
print(emp_1.fullname)	## here email is instance method not attribute but able to access as attribute because of @property

del emp_1.fullname