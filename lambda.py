#lambda expreession

#filter function
mylist =[1,2,3,4,5,6,7,8,9]

def even_number(num):
    return num%2 == 0

even = filter(even_number,mylist)
print(list(even))

evens = filter(lambda num:num%2 == 0,mylist)
print(list(evens))
