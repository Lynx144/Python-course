def xu_ly_so_chan_le(danh_sach_so: list[int]) -> list[int]:
    res=[]
    for i in danh_sach_so:
        if i %2==0:
            res.append(i)
        else:
            res.append(i*2)
    return res
x =[ 1,2, 3, 4, 5, 6]
print(xu_ly_so_chan_le(x))
