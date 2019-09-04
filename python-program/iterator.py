#https://www.youtube.com/watch?v=jTYiNjvnHZY
# list is iterable but not iterator. iterator has next() to get next element
# list tuple dictionary, file etc are iterable
# if anything is iterable => must have a special method __iter__

a= [1,2,3] # list is iterable not iterator
# to know property of anything
print(dir(a))
# print(next(a)) # TypeError: 'list' object is not an iterator

# to make it iterator 
a_iterator = a.__iter__() # =>__iter__() same as iter(a)
# a_iterator = iter(a) # both are same it has next() and when exhausted stopiterator error comes
print(a_iterator)
print(dir(a_iterator))
# print(next(a_iterator))
# print(next(a_iterator))

while True:
	try:
		item = next(a_iterator)
		print('item : ',item)
	except StopIteration:
		break

# practice iterator
class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


def my_range(start):
    current = start
    while True:
        yield current
        current += 1


nums = my_range(1)

for num in nums:
    print(num)

