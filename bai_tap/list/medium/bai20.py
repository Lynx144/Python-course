x = [1, 3, 2,1]
a = False
for z in range(0, len(x)):
    for y in range(z+1, len(x)):
        if x[z] == x[y]:
            a = True
            break
print(a)