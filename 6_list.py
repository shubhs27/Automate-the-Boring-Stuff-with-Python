print("lists are mutable")

a,b=10,20
print(a,b)
a,b= b,a
print(a,b)
print()

print(list(range(1,20,2)))
print()

l1= list(range(5))
l2= l1
l2[1]= "wtf"
print(l2)
print(l1)

def func(l):
    l.append("thats crazy")
func(l2)
print(l2)

import copy
l3= copy.deepcopy(l2)

func(l3)
print(l3)
print(l2)
print()

print("The \ char is used to",\
      "continue or stretch instruction",\
      "across multiple lines")