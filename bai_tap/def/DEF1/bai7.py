def kiem_tra_palindrome(s) -> bool:
    res=''
    for a in s:
        res = a+ res 
    if res == s:
        return True
    return False
s =input('Nhập chữ: ')
res =kiem_tra_palindrome(s)
print(kiem_tra_palindrome(s))