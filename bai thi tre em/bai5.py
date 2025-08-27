kg= int(input('Nhập cân nặng của bạn: '))
m= int(input('Nhập chiều cao của bạn của bạn: '))
m = float(m/100)
if kg/m**2 <18.5:
    print("Gầy")
elif kg/m**2 <25:
    print("bình thường")
else:
    print("Trà bông")