def Giai_thua(x)->int:
    ans=1
    for i in range(1,x+1):
        ans*=i
    return ans
x=int(input('Insert a number: !'))
print(Giai_thua(x))