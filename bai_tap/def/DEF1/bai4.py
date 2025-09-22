def tinh_giai_thua(n) -> list:
    res=1
    for x in range(1,n+1):
        res = x * res
    return res
n= int(input('Nhập số: '))

print(tinh_giai_thua(n))