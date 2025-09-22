def NT(n) ->bool:
    if n <2:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True 
def x(a,b)->list[int]:
    res=[]
    for e in range(a,b+1):
        if NT(e):
            res.append(e)
    return res
a= int(input('Nhập số: '))
b= int(input('Nhập số: '))
print(x(a,b))