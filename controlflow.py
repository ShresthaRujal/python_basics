#if condition
if 1<2: # : indents next line
    print('True!')
elif 3==3:
    print('élse if')
else:
    print('False!')

#for Loop
sequence = [1,2,3,4,5,6]
for item in sequence:
    print(item)

#forloop in dictionary
d = {"sam":1,"jan":2,"fan":3}
for item in d:
    print(item) #keys
    print(d[item])

#tuples unpacking
pairs = [(1,2),(3,4)]

for (tup1,tup2) in pairs:
    print(tup1)
    print(tup2)

#while
i =1
while i<5:
    print("i is {}:".format(i))
    i = i+1

#generating numbers
print(list(range(5)))
print(list(range(0,20,2)))

for item in range(10):
    print(item)
