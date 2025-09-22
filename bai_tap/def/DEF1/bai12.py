def dem_so_lan_xuat_hien(danh_sach: list, phan_tu: any) -> int:
    res=0
    for i in danh_sach:
        if i == phan_tu:
            res+=1
    return res
x =[1, 2, 2, 3, 2, 4]
y= int(input('Nhập số muốn kiểm tra: '))
print(dem_so_lan_xuat_hien(x,y))