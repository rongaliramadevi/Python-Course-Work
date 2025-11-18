#Type conversion
#Numeric values only converted into numeric types not collections, and collections converted into only colections not numeric type


a=10
print(float(a))
print(str(a))
print(complex(a))
print(bool(a))
#int cant be converted into list, set, tuple , dictionary  beacuse they are collections , int is a single varible cant iterable

b=12.5
print(int(b))
print(str(b))
print(complex(b))
print(bool(b))
#float cant be converted into list, set, tuple , dictionary  beacuse they are collections , int is a single varible cant be iterable
s='Python'
print(list(s))
print(tuple(s))
print(set(s))
print(bool(s))

l=[1,2,3,4,5]
print(str(l))
print(tuple(l))
print(set(l))
print(bool(l))

t=(1,2,3,4,5)
print(str(t))
print(list(t))
print(set(t))
print(bool(t))

S={1,2,3,4,5}
print(str(S))
print(list(S))
print(tuple(S))
print(bool(S))

d=[(1,2),(3,4),(5,6),(7,8)]
print(dict(d))
d={1:1,2:4,3:9}
print(list(d))
print(tuple(d))
print(set(d))