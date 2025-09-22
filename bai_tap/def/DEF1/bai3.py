def tim_lon_nhat(x , y) -> int:
    return x if x >y else y
a= int(input('Nhập số: '))
b= int(input('Nhập số: '))
print(tim_lon_nhat(a,b))