list = ["rujal shrestha",1,2,3,True,["go","to","the","zoo"]]
print(list)

#indexing
print(list[4:])

#append
list.append("OK?");
print(list)

#extend
list.extend(["hello","tiger"])
print(list);

#pop
list.pop(4)
print(list)

#reverse
list.reverse()
print(list)

#sort
numberList=[3,5,1,6,7]
numberList.sort()
print(numberList)

#list comprehension
nestedList = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in nestedList]
print(first_col)

#normal example
x =[1,2,3,4]
out=[]
for item in x:
    out.append(item**2)

print(out)

#comprehension mode
out =[item**2 for item in x]
print(out)
