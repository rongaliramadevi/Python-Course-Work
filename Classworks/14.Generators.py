def reels(data):
    for i in data:
        yield i

data=['1..100','100..200','200..300','300-400','400-500']
scroll=reels(data)

# print first 5 items
for _ in range(len(data)):
    print(next(scroll))

while True:
    ch = input("[s]croll or [b]ack: ").lower()
    if ch == 's':
        try:
            print(next(scroll))
        except StopIteration:
            print("No more reels!")
    else:
        print("Exit")
        break

