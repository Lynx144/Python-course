x= int(input('Nhập bán kính: '))
import math
def Sop(x)->float:
    s = math.pi * (x**2)
    return s

print(f"Diện tích của hình tròn là {Sop(x)}")