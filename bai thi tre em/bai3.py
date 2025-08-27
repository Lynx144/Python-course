i = int(input("Nhập số km bạn muốn đi: "))
kq= 0
if i ==0:
    print("Không hợp lệ")
elif i == 1:
    print("Số tiền bạn cần trả là 15000")
else:
    kq = kq + (i-1) * 12000 + 15000
    print(f"Số tiền bạn cần trả là {kq}")