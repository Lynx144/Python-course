def tim_lon_thu_hai(x:list[int]) -> int:
   a=[]
   a.append(min(x))
   a.append(max(x))
   for i in x:
      if i not in a:
         return i
x = [10,3,1]
print(tim_lon_thu_hai(x))