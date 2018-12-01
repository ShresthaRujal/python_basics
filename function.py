def my_func(param = 'Rujal'):
    """ Multiline comment """
    return "hello {}!".format(param)

result = my_func()
print(result)

#types
def addNumber(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "input is invalid"

print(addNumber(2,3))
