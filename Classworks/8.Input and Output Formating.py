#input formating

s=input("Python") #string
print(s)

i=int(input()) #integer

i=float(input()) #float

l=list(map(int,input().split(','))) #list 

name=input("Enter name:")
print(name)
age=int(input("Enter age:"))
print(age)

names=input("ruchitha, preethi, varsha")

print(names)

names=list(map(int,input().split()))
print(names)

names=tuple(input().split())#tuple input for str
print(names)

names=set(map(int,input().split())) #set input()
print(names)

d=eval(input())
{'name':'rama','age':21}
print(d)

a,b=list(map(int,input().split())) #multiple varibles assignment
#output formating
a=10
b=20
c=30
print(a+b)
print(a,b)
print("a=",a,"b=",b)
print(f'a={a}\nb={b}\nc={c}') #f strings
print('a={}\nb={}\nc={}'.format(a,b,c)) #formating
