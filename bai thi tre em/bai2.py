a = int(input("NHập A:"))
b=int(input("NHập B:"))
if a != 0:
    if b == 0 :
        print("x=0")
    else:
        print(f"x={-b/a}")
elif a == 0 and b ==0:
    print("Phương trình này vô số nghiệm")
else:
    print("Phơng trình này vô nghiệm")