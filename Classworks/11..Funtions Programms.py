def leng(s):
    c=0
    for i in s:
        c+=1
    return c
s="Ramadevi"
print("length of:",leng(s))

2.
l=list(map(int,input().split()))
d=list(map(lambda i:i+i,l))
print(d)

3.
def remo(l, e):
    l.remove(e)
    return l

l = list(map(int, input("Enter list: ").split()))
e = int(input("Enter element to remove: "))
print(remo(l, e))


4.
def update(d):
    for i in d:
        d[i]+=1
    return d
d={'a':7,'b':18,'c':23}
print(update(d))


5.
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(fact(5))
print(fact(6))
print(fact(7))

#6.fibaonacci
n=int(input("enter the nth term:"))
a=0
b=1

for i in range(n-2):
    c=a+b
    print(c,end=' ')# 0 0 1 1 2 3 5 8 13 21 34
    a=b
    b=c
    

n=int(input("enter the nth term:"))
a=0
b=1

7.
for i in range(n-2):
    c=a+b
    
    a=b
    b=c
print(c,end=' ')#34

#8.sum of numbers
def add(a,b):
    return a+b
a=int(input())
b=int(input())
print(add(a,b)) 

#9.square of a number
def sq(n):
    return n**2
n=int(input())
print(sq(n))

#10.Area of a circle
def are(r):
    a=3.14*r*r
    return a
r=float(input())
print(are(r))

11.

def greet(name):
    print(f'Hello {name}')
    return
name=input("enter name:")
greet(name)


#12.Celsius to Fahrenheit
def c_to_f(c):
    return (c*9/5)+32
c=float(input("enter c:"))
print(c_to_f(c))

#13.simple intrest

def simple(p,t,r):
    si=(p*t*r)/100
    return si
p=int(input())
t=int(input())
r=int(input())
print(simple(p,t,r))

#14.append ele to a list
def lis(l,n):
    l.append(n)
    return l
l=list(map(int,input("enter list:").split(",")))
n=int(input("enter no:"))
print(lis(l,n))

#15.
def sor(l):
    l.sort()
    return l
l=list(map(int,input().split(",")))
print(sor(l))

#16.clear list
def cle(l):
    l.clear()
    return l
l=l=list(map(int,input("enter list:").split(",")))
print(cle(l))