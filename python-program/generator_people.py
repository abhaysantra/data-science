import mem_profile
import random
import time

#### generator is iterator with yeild method no next method
# def square_numbers(nums):
#     for i in nums:
#         yield (i*i)

# my_nums = square_numbers([1,2,3,4,5])

my_nums = (x*x for x in [1,2,3,4,5])

print list(my_nums) # [1, 4, 9, 16, 25]

# for num in my_nums:
#     print num

a = [1,2,3,4,5]
# square = [(i*i) for i in a] # here square is list
# print(square)
square = ((i*i) for i in a) # here square is generator
print(square)
#to make generator as list
# square_data = list(square)
for i in square:
    print (i)


names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print ('Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil()))

def people_list(num_people):
    result = []
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

# t1 = time.clock()
# people = people_list(1000000)
# t2 = time.clock()

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

print ('Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil()))
print ('Took {} Seconds'.format(t2-t1))
