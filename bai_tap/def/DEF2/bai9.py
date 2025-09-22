def tinh_tong_theo_nguong(danh_sach: list[int], nguong: int) -> int:
    res = 0
    for i in danh_sach:
        if i > nguong:
            res +=i
    return res
a= [1, 2, 3, 4, 5]
b = 3
print(tinh_tong_theo_nguong(a,b))

