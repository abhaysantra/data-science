# https://realpython.com/primer-on-python-decorators/
import os, sys

print('.........decorator without arguments..............')
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

# @my_decorator => say_whee = my_decorator(say_whee)
say_whee()
print('.....................decorator with arguments.........')

def my_decorator_with_arg(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator_with_arg
def say_whee_with_arg(arg,kwargs):
    print("Whee! ",arg, kwargs)

dict_data = {'1':'Monday', '2':'Sunday', '3':'Tuesday'}
dict_data1 = {'1':'abhay','2':'Bisu', '3':'Kaka'}
# @my_decorator => say_whee = my_decorator(say_whee)
say_whee_with_arg("I am in this world !!!", dict_data)

print('................decorator with return values............')
def my_decorator_with_arg_and_return_val(func):
    def wrapper(*args, **kwargs):
        print("before the function is called.")
        return func(*args, **kwargs)
        print("after the function is called.")
    return wrapper

@my_decorator_with_arg_and_return_val
def say_whee_ret_val(arg,kwargs):
    print("Whee! ",arg, kwargs)
    print(f"Hello............: {arg}..{kwargs}")
    return arg

ret_val = say_whee_ret_val("I am in this world !!!", dict_data)
print('Ret Val : ',ret_val)