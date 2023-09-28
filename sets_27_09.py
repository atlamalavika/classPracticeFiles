a=set()
print(type(a))
a={}
print(type(a))
a=[1,2,3]
print(set(a))
b={2,3,4}
b.add(7)
print(b)
c={4,5,6}
c.update({9})
print(c)
d=c.copy()
print(id(c))
print(id(d))

c.remove(9)
print(c)

d={1,2,3}
d.discard(2)
print(d)

d.discard(10)
print(d)

#set operations
a={1,2,3,4}
b={5,6,7,8,1,2}
print(a.union(b))
print(a|b)
print(a.intersection(b))
print(a&b)
print(a.difference(b))
print(a-b)
print(a.symmetric_difference(b))
print(a^b)