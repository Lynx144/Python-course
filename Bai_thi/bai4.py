def print_but_better(a)->int:
    x=[]
    for i in range(1,101):
        if i%2==0:
            x.append(i)
    return x
x=0
print(print_but_better(x))