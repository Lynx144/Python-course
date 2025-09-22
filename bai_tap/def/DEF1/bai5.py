def dem_nguyen_am(n) -> int:
    res=0
    for i in n:
        if i in ['a','e','i','o','u','A','E','I','O','U']:
            res +=1
    return res
n = input('Nhập chữ: ')
print(dem_nguyen_am(n))