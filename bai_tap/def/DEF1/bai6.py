def dao_nguoc_chuoi(s) -> str:
    res=''
    for a in s:
        res= a +res
    return res
s=input("Nhập chữ:")
print(dao_nguoc_chuoi(s))