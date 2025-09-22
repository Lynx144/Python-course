def tim_min_list(l: list[int]) -> int:
    res = 999999999999999999999999
    for i in l:
        if i < res:
            res = i
    return res
l= [5, 2, 9, 1, 7]
print(tim_min_list(l))