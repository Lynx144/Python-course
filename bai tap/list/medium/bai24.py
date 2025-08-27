a = [10, 20, 30, 20]
b =int(input('Nhập số: '))
c=[]
id = 0
for x in range(0,len(a)):
    if a[x] not in c:
        c.append(a[x])
    else:
        id =x
        break
print(id)