def shooting(bullets):
    if bullets<=0:
        print("game over")
        return
    print(f'{bullets} are left')
    shooting(bullets-1)
shooting(10)

#2.
def display(n):
    if n>10:
        print("stop")
        return
    print(n)
    display(n+1)
    
display(1)



#3.
def display(n):
    if n>10:
        print("stop")
        return
    
    display(n+1)
    print(n)
    
display(1)


#4.
def display(n,i):
    if i>=len(n):
        print("stop")
        return
    print(n[i])
    display(n,i+1)
   
display("codegnan",0)


#5.
def display(n,i):
    if i>len(n):
        print("stop")
        return
    print(n[:i])
    display(n,i+1)
display("abcde",1)



#6.
def display(n,i):
    if i>len(n):
        
        return
   
    display(n,i+1)
    print(n)
    
display("abcdefgh",4)