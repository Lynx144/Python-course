def loc_so_chan(danh_sach_so: list[int]) -> list[int]:
    res=[]
    for i in danh_sach_so:
        if i %2==0:
            res.append(i)
    return res
a = [1, 2, 3, 4, 5, 6]
print(loc_so_chan(a))