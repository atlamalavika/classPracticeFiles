#map
def square(x):
    return x*x
lis=[1,2,3,4,5,6]
result=map(square,lis)
print(list(result))

 #reduce
list1=[1,2,3,4,5,6]
from functools import*
def add(x,y):
   return x+y
result1=reduce(add,list1)
print(result1)
print(reduce(lambda x,y:x+y,list1))

#filter
list3=[1,2,3,4,5,-7,-8,-9]
def minus(x):
    return x>0
a=filter(minus,list3)
print(list(a))
