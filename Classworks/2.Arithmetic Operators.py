c=30
d=40

print('c<d:', c<d) # c<d: True
print('c>d:', c>d) # c>d: False
print('c<=d:', c<=d) # c<=d: True
print('c>=d:', c>=d) # c>=d: False
print('c==d:', c==d) # c==d: False
print('c!=d:', c!=d) # c!=d: True

# 3.Assignment Operator

'''
var=var op val
var op = val
'''
e=100
e+=100
print('e+=100:',e) # e+=100: 200
e-=100
print('e-=100:',e) # e-=100: 100
e*=100
print('e*=100:',e) # e*=100: 10000
e//=100
print('e//=100:',e) # e//=100: 100
e**=3
print('e**=100:',e) # e**=100: 1000000
e%=100
print('e%=100:',e) # e%=100: 0
e/=100
print('e/=100:',e) # e/=100: 0.0


#4.Logical Operators


x=100
y=50

print('x%20==0 and y%20==0:', x%20==0 and y%20==0) # x%20==0 and y%20==0: False
print('x%20==0 or y%20==0:', x%20==0 or y%20==0) # x%20==0 or y%20==0: True
print('not x%20==0:',not x%20==0) #  not x%20==0: False
print(' not y%20==0:', not y%20==0) # not y%20==0: True

#Membership Operators

s='Python Programming'
print(" 'i' in s:",'i' in s) #'i' in s:True
print(" 'x' not in s:", 'x' not in s) #'x' not in s:True

l = {1, 2, 3, 4}
print("3 not in l:", 3 not in l)   # 3 not in l: False

s = {10, 20, 30, 40}
print("40 in s:", 40 in s)           # 40 in s: True
print("50 not in s:", 50 not in s)   # 50 not in s: True

d = {1:2, 4:3, 9:4, 16:25}
print("1 in d:", 1 in d)             # 1 in d: True
print("4 not in d:", 4 not in d)     # 4 not in d: False

#Identity Operators 


a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
c = a

print('a is b:', a is b)    # a is b: False
print('a is c:', a is c)    # a is c: True

print('id(a):', id(a))  # id(a): 1427474992192
print('id(b):', id(b))  #id(b) : 1427520075328
print('id(c):', id(c))  # id(c): 1427474992192

print('a is not b:', a is not b)   # a is not b: True
print('a is not c:', a is not c)   # a is not c: False


# Bitwise Operatoes($ | ^ ~ << >>)
'''0 - 0000
1 - 0001
2 - 0010
3 - 0011
4 - 0100
5 - 0101
6 - 0110
7 - 0111
8 - 1000
9 - 1001
10 - 1010   
11 - 1011
12 - 1100
13 - 1101
14 - 1110
15 - 1111

# & (AND Gate)
00 - 0
01 - 0
10 - 0
11 - 1


4-0100
5-0101
   0100
-------------------
|-Gate
00-0
01-1
10-1
11-1

11-1011
12-1100
   1111
-------------------
^-Gate
00-0
01-1
10-1
11-0

14-1110
15-1111
   0001
-------------------
~-Gate
0-1
1-0

<<-shift
8<<2-1000
100000-32

>>-shift
8>>2-1000
10-2'''

print('4&5:', 4 & 5) #4&5: 4
print('11|12:', 11|12) #11|12: 15
print('14^15:', 14^15) #14^15: 1
print('~16:', ~16) #~16: -17
print('8<<1:', 8<<1) #8<<1: 16
print('16>>1:', 16>>1) #16>>1: 8




























