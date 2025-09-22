def dao_nguoc_tung_tu(cau: str) -> str:
    res=[]
    a = cau.split(' ')
    for i in a :
        res.append(i[::-1])
        
    return ' '.join(res)
print(dao_nguoc_tung_tu('Hello World'))