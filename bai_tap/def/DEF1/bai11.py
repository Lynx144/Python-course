def kiem_tra_nam_nhuan(nam: int) -> bool:
    if nam %4==0 or nam % 100==0:
        return True
    return False
a = int(input('Nhập năm muốn kiểm tra: '))
print(kiem_tra_nam_nhuan(a))