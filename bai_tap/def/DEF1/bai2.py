def kiem_tra_so(so)->str:
    return "chan" if so%2==0 else "le"
a=int(input("Nhập số: ")) 
print(kiem_tra_so(a))