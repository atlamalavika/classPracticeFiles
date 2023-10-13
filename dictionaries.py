word={}
print(type(word))
word["emp1"]="malavika"
word["emp2"]="rahul"
word["emp3"]="kavya"
word[104]="shiva"
print(word)
#updating value
word["emp1"]="manu"
print(word)
#accessing
print(word["emp1"])
#delete key
del word["emp1"]
print(word)
#clear dictionary
word.clear()
print(word)

#get()
word1={101:"mal",102:"kav",103:"raj"}
print(word1.get(101))
print(word1.get(105))
print(word1.pop(102))
print(word1.popitem())
#Accessing items
print(word1.keys())
print(word1.values())
print(word1.items())

#take
word3={}
for i in range(3):
    key=input("enter: ")
    value=input("enter: ")
    word3[key]=value
print(word3)