def kiem_tra_so_dac_biet(so: int) -> str:
    res=''
    if so %2 ==0:
        res = 'Chẵn'
        return res
    else :
        if so %3==0:
            res='Lẻ và Bội của 3'
            return res
        res ='Lẻ'
        return res
so = int(input('Nhập số: '))
print(kiem_tra_so_dac_biet(so))