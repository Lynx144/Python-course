def tao_chuoi_tu_list_loc(list_tu: list[str], do_dai_toi_thieu: int) -> str:
    res=[]
    for i in list_tu:
        if len(i) >= do_dai_toi_thieu:
            res.append(i)
    return ' '.join(res)
x= ["Hello", "a", "World", "is", 'GYAtt']
y=3
print(tao_chuoi_tu_list_loc(x,y))