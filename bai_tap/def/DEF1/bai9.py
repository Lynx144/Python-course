def tinh_tong_list(danh_sach) -> list[int]:
    res=0
    for i in danh_sach:
        res+=i
    return res
danh_sach=[1,2,3,4,5]
print(tinh_tong_list([1,2,3,4,5]))