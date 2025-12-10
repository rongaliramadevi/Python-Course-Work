#for with else

pro=['laptop','mpuse','keypad','speaker']
s=input("Enter the product:").strip()

for i in pro:
    if i==s:
        print("Product found! shop now")
        break
    print(i)
else:
    print("End of the products. The item you search for is not found")


#while with else

i=0
while i<5:
    if i==3:
        break
    print(i)
    i+=1
else:
    print("end of nums:")