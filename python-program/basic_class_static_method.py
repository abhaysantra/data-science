#https://realpython.com/lessons/what-are-these-different-method-types-good-python/

class MyClass():
	#instance method
	def instance_method(self):
		print ('instance_method called ',self)

	@classmethod
	def classmethod(cls): 	# cls and MyClass both are same instead of cls we can use MyClass
		print('class method :',cls)
		
	@staticmethod
	def staticmethod():
		print('staticmethod...')

obj = MyClass()
obj.instance_method()
#instance_method called  <__main__.MyClass object at 0x7f8adeee23c8>
obj.classmethod()
#class method : <class '__main__.MyClass'>
obj.staticmethod()
#staticmethod
MyClass.classmethod()
#class method : <class '__main__.MyClass'>
MyClass.staticmethod()
#staticmethod
MyClass.instance_method()
#error : TypeError: instance_method() missing 1 required positional argument: 'self'
