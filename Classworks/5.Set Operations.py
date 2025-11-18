'''
Set
---
'''

s=set() 
print(s)#set()
s={1,2,3,4,5,6,7}
print(s)#{1, 2, 3, 4, 5, 6, 7}
s={1,1,1,2,3,4,4,5,6,7,7}
print(s)#{1, 2, 3, 4, 5, 6, 7}

#set properties
1.#unordered

s={100,4000,12,56,12,45,18}

#Mutable
print(s)#{4000, 18, 100, 56, 12, 45}
s.remove(4000)
print(s)
s.add(12.23)
print(s)
s.add("124")
print(s)
s.add(False)
print(s)
s.add(None)
print(s)
s.add((1,2,3,4))
print(s)

#operations on set

girls={'ruchitha','Rama','Priya','Fareen','Krishna','prameela','Geetha'}
guys={'rakesh','pundri','mani','ramesh','harish','venkat','vinay'}
guys.add('prabhas')
online={'prabhas','naidu'}
print(girls)
print(guys)
print(online)
print('Rama' in girls)
print('rajesh' in guys)
print(girls | guys)
print(girls.union(guys))
print(online.intersection(guys))

print(guys.difference(online))
print(guys.symmetric_difference(online))
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a.symmetric_difference(b))
print(a.difference(b))

a={1,2,3,4}
b={2,3}
print(a.issubset(b))
print(b.issubset(a))
print(girls.isdisjoint(guys))
print(guys.isdisjoint(online))

#Built in Methods

print(girls)
print(girls.add('sahithi'))
print(girls.add('meggi'))

print(girls.remove('ruchitha'))
print(girls.discard('ruchitha'))
print(girls.pop())
print(online)
print(online.clear())
print(guys)
print(guys.update({'shive','vasu','sathish'}))
print(guys)
c=[1,2,3,5,6]
max(c)
min(c)
sum(c)
sorted(c)
s=[1,2,3,4]
print(set(s))

