def tim_min_va_vi_tri(danh_sach: list[int]) -> list:
    res = min(danh_sach)
    a =[]
    for i in danh_sach:
        if i == min(danh_sach):
            a.index(i)
            a.append(res)
            return a
x = [3,9,1,3]
print(tim_min_va_vi_tri(x))