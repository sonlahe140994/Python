a1 = [1,4,5,6,2,5,6,7,8,2,1,4,5,6]
a2 =[2,5,6,7,8,955,12,44,2,43,21]
a3 = []
for i in a1:
    if i in a2 and i not in a3: a3.append(i)


for i in a3: print(i)