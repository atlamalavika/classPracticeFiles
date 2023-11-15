def find(x):
    if x==1:
        return 1
    return (x)*find(x-1)
num=5
num1=find(num)
print(num1)


s=lambda n2:n2*n2
print(s(9))
l=lambda x,y:x+y
print(l(1,2))

from functools import *
import random
print(random.random())