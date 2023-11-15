# #end operator
n=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j],end="")

# #list comprehenion
name=["mala","parveen","surya","bhargav"]
new_list=[j for j in name if "a" in j]
print(new_list)
a=[20,30,40]
str1=""
for i in a:
    i1=str(i)
    str1+=i1
print(str1)

