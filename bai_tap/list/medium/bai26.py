a = [10, 20, 30, 40, 50]
b= [1, 3]
c=[]
for i in range(len(a)):  
    if i not in b:
        c.append(a[i])
print(c)

