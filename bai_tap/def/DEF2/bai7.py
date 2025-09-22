def kiem_tra_palindrome_nang_cao(s: str) -> bool:
    q=s.lower()
    b=[]
    res=''
    for e in s:
        b.append(e)
    a= s.split(' ')
    for i in s:
        res= i+res
    if res == q:
        if len(b) <5:
            return False
        else:
            return True
    else:
        return False
print(kiem_tra_palindrome_nang_cao("mam"))