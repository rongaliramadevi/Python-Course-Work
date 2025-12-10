#lambda functions
def wish(name):
    print(f'welcome to python {name}')
wish("rama")
wish("priya")
wish("fareen")


#lambda functions
wish=lambda name: f'welcome to python {name}!'
print(wish("rama"))

#2.
def sq(n):
    print(f'squares of a numbers is {n*n}')
sq(6)

lsq=lambda n: f'squares of a number is {n*n}'
print(sq(7))

#3.
add=lambda a,b:a+b
print(add(7,3))

#4.
a=lambda r:3.14*r*r
print(a(15))
print(a(5))

#5.
eord=lambda n:"even" if n%2==0 else "odd"
print(eord(7))

#6.
v='aeiouAEIOU'
vc=lambda ch:"vowel" if ch in v else "con"
print(vc("a"))

#7.#map 
l=[1,2,3,4,5]
res=list(map(lambda i: f'{i}%',l))
print(res)

#8.
n=['rama devi',' krishna priya','sheik fareen']
res=list(map(lambda i: i.title(),n))
print(res)

#9.
p=[20000,30000,40000]
res=list(map(lambda i:f'${ i+i*0.18}',p))
print(res)

#10.#filter

l=[1,2,3,4,5]
res=list(filter(lambda i:i%2==0,l))
print(res)

#11.
n=['rama devi',' krishna priya','sheik fareen']
res=list(filter(lambda i:i[0]=='r',n))
print(res)

#12.
p={
    'milk':20,
    'bread':30,
    'soap':10,
    'butter':15,
    'headsets':0,
    'sugar':0,
    'salt':1,
    'chilli powder':0
    }
res=list(filter(lambda i:p[i]!=0,p))
res1=list(filter(lambda i:p[i]==0,p))
print(res)
print(res1)

#13.
from functools import reduce
l=[1,2,3,4,5]
lan=['java','python','c','csharp','javascript']
res=reduce(lambda a,b: a+b,l) #first it ass 1,2 and stro result ans a than add 3, 3 and store in a like that
res1=reduce(lambda a,b: a+' '+b,lan)
res2=reduce(lambda a,b:a*b,l)
print(res)
print(res1)
print(res2)

#14.

d={
    'pravenn':80,
    'rama':87,
    'manoj':89,
    'priya':92,
    'fareen':86
}
print(d.items())
print(dict(sorted(d.items(),key=lambda i:i[0])))
print(dict(sorted(d.items(),key=lambda i:i[0],reverse=True)))

print(dict(sorted(d.items(),key=lambda i:i[1])))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))