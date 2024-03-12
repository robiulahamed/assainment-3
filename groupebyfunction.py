from itertools import groupby
strings=['Dhaka','cumilla','chattogram','khulna','barisal','sylhet']
strings.sort(key=len)

group_str= groupby(strings,key=len)

print("the groups based on strings : ")
for i ,j in group_str:
    print(f"Length {i}:{', '.join(j)}")