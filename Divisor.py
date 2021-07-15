
while True:
    try:
        num = int(input("Enter number: "))
        break
    except Exception as e:
        print(str(e))

print(num)

x = range(1,100)
for i in x: 
    if i%num==0:print(i)