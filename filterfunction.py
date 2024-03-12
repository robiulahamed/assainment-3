def is_even(num):
    return num%2==0


numbers =[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
chek_even_num=list(filter(is_even,numbers))
print("the orginal number :", numbers)
print("the even number: ",chek_even_num)
