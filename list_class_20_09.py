
#taking input
a=eval(input("enter: "))
print(a)

#count
count1="malavika"
b=count1.count("a")
print(b)

count2=["a",1,"a","a",2,3]
print(count2.count("a"))

#step indexing
a=[1,2,3,4,5,6,7,8,9,10]
a1=a[1:10:2]
print(a1)

#first occurance
a2=[1,2,3,4,5,2,2]
b1=a2.index(5)
print(b1)

#insert value at particular index
a2.insert(2,"apple")
print(a2)
a1=(1,2,3)
print(a1.insert(2,"india"))