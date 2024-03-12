from functools import reduce

def red_fun(a,b):
    return a*b

numbers=[1,2,3,4,5,6]
red_elm=reduce(red_fun,numbers)
print("the orginan numbers: ",numbers)
print("product of all element : ",red_elm)
