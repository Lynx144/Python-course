def tinh_tong_tru_boi_5(n: int) -> int:
    res=0
    for i in range(1,n+1):
        if i %5 !=0:
            res +=i
    return res
n = int(input('Nhập số: '))
print((tinh_tong_tru_boi_5(n)))