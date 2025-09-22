def FB(a)->str:
    res= []
    for i in range(1,a+1):
        if i %3 == 0 and i %5 == 0:
                res.append('FizzBuzz')
        elif i %5 == 0:
                res.append('Buzz')
        else:
            if i %3 == 0:
                res.append('Fizz')
            else:
                 res.append(i)
    return res
a= int(input('Nhập số: '))
print(FB(a))