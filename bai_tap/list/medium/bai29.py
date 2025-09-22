x= [1, 2, 3, 4, 5]
a= 0
b=0
for y in x:
    if y%2 == 0:
        a+=y
    else:
        b+=y
print(f'Tổng các só chẵn là: {a}')

print(f'Tổng các só lẻ là: {b}')
