from functools import chain

list_1=[10,20,30]
list_2=['x','y','z']
list_3=[True,False,True]

conbined_ite=chain(list_1,list_2,list_3)

print("the combined iterable list : ")
for i in conbined_ite:
    print(i)