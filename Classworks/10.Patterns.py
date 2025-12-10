#1.
n=int(input("Enter the size:"))
for row in range(5):
    for col in range(5): 
        print(col, end=' ')
    print()
#.output
'''0 1 2 3 4 
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4'''
        
    
#2.
n=int(input("Enter the size:"))
for row in range(0,5):
   for col in range(row+1):
       print(col, end=' ')
   print() 

#3.
n=int(input("Enter the size:"))
for row in range(n):
   for col in range(n-row):
       print(col,end=' ')
   print()

#4
n=int(input("Enter the size:"))
for row in range(n):
    for spc in range(n-1-row):
        print(' ',end=' ')
    for col in range(row+1):
       print('*',end=' ')
    print() 

#5

n=int(input("Enter the size:"))
for row in range(n):
    for spc in range(row+1): #or row
        print(' ',end=' ')
    for col in range(n-1-row):#or n-row
       print('*',end=' ')
    print()

#6.

n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1:
            print('*',end=' ')
        else:
            print(' ', end=' ')
    
    
    print() 


#7.
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1 or row==n//2:
            print('*',end=' ')
        else:
            print(' ', end=' ')
    
    
    print()

#8.
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row+col==n-1:
            print('*',end=' ')
        else:
            print(' ', end=' ')
    
    
    print() 

#9.

n=int(input())
for i in range(n):
    for j in range(n):
        if j%2:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print() 

#10.

n=int(input())
for i in range(n):
    for j in range(n):
        if i<j:
            print(0,end= ' ')
        else:
            print(1, end=' ')
    print()  