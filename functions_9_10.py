#function
def even_fun(x):
    if x%2==0:
        print("even")
    else:
        print("odd")
even_fun(3)

#ARGUMENTS
#1.POSITIONAL ARGUMENT
def sub(x,y):
    print(x-y)
    print(y-x)
sub(100,200)

#2.keyword arguments
def sub(x,y):
    print(x-y)
    print(y-x)
sub(y=100,x=200)

def wish(name,msg):
    print("hi",name,msg)
wish("good evening","malavika")#positional
wish(msg="malavika",name="yadav")#key word
wish("praveen",msg="yadav")#positional,keyword


#3.variable length arguments:The arguments passsed to the 
# function are packed as tuple and we can iterate through it
def sum(*n):
    sum=0
    for i in n:
        sum+=i
    print(sum)
sum()
sum(10,20)
sum(10,20,30)

#4.keyword varibale length arguments
#we can pass any number of keyword arguments 
#internally this arguments stored as keyand value pairs
#arguments passed are packed as dictonary
def display(**m):
    for k,v in m.items():
        print(k,"-",v)
display(id1="malavika",id2="rahul",id3="kavya")
   