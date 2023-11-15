main=input("enter: ")
sub=input("enter: ")

empty=[]
for i in range(len(main)-(len(sub)-1)):
    i1=main[i:len(sub)+i]
    empty.append(i1)
print(empty)
print(empty.count(sub))