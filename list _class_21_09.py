# 1.extend() adds 2 list
a1=[1,2,3]
b1=[4,5,6]
a1.extend(b1)
print(a1)
print(a1+b1)
# 2.remove()we can remove particular char cannot remove value at particular index
a2=[1,2,3]
a2.remove(1)
print(a2)

#3.pop()==removes the last element
a3=[1,2,3]
a3.pop()
print(a3)

a31=[1,2,3,4] #remove element at particular index
a31.pop(1)
print(a31)

#4.ordering elements from list
a=[1,2,3,4,5]
a.reverse()
print(a)

#5.sorted
a5=[8,9,6]
a5.sort()
print(a5)

#6.aliasing and clonning :id will same for aliasing 
#so it will effect original value so we use clonning
a6=[1,2,3]
a61=a6
print(id(a6))
print(id(a61))
#clonning:copy()
a62=[1,2,3]
a63=a62.copy()
print(id(a62))
print(id(a63))


#7.clear() clear the list and return empty list
a7=[1,2,3]
a7.clear()
print(a7)



#9.comparing list
a9=[1,2,3,4]
a91=[1,2,3,4,5]
print(a9>a91) #false compare list length

a92=[1,2,3]
a93=[1,3,4]
print(a92<a93) #true if first char same then compares second char

a93=["dog"]
a94=["Dog"]
print(a93>a94) #true "d husky value greater than D"
#8.deleting list
a8=[1,2,3]
del a8



 