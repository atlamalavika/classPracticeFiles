word=("mal",2,3.4,True)
print(type(word))
w1=("mal",)
print(type(w1))
#accessing
w2=(1,2,3,4,5)
print(w2[::-1])
#add
print((1,2,3)+(4,5,6))
#functions
main=(1,2,3,4)
print(len(main))
print(main.count(1))
print(main.index(1))
print(sorted(main))
print(min(main))
print(max(main))

#packing and unpacking
#packing :the process of assigning values to a tuple is known as packing
emp1,emp2,emp3,emp4=("mala","kav","bhar","nar")
#unpacking:the process of assigning  values in tuple to left side variables
emp1,*emp2=("mala","kav","bhar","nar")
print(emp1)
print(emp2)
