def tinh_tong_co_gioi_han(a: int, b: int, gioi_han_tong: int) -> int:
    res =0
    res = a+b
    if res >=gioi_han_tong:
        res=0
        return res
    return res
a= int(input('Nhập số: '))
b=int(input('Nhập số: '))
c=int(input('Nhập số giới hạn : '))
print(tinh_tong_co_gioi_han(a,b,c))