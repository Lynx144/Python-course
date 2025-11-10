def Vip_pro_print(a)->list:
    x=[]
    ans=0
    for i in range(1,11):
        x.append(f"{a}*{i}={a*i}")
    return x
a=int(input('Insert a Random number: '))
print(Vip_pro_print(a))