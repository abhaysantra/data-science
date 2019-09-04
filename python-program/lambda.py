# lambda function: => anonimous one liner single use function

# normal function
def second_element(x):
	print(x)
	return x[1]

a = [(2,3),(4,3),(6,2)]
a.sort(key = second_element)
print(a)

# using lambda
a = [(2,3),(4,3),(6,2)]
a.sort(key=lambda a : a[0])
print('lambda output : ', a)
