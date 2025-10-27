van_ban = "Python la mot ngon ngu lap trinh Python rat pho bien"
x=van_ban.split()
for i in x:
    a={}
    if i not in a:
        a[i]=1
    else:
        a[i]=x.count(i)
print(a)