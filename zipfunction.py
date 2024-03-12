def ke_val_dictt(a,b):
    return dict(zip(a,b))

def ke_val_lis(a,b):
    return list(zip(a,b))     

keys=[1,2,3,4,5,6,7]
values=[10,20,30,40,50,60,70]
ke_values=ke_val_dictt(keys,values)

print("the resultin dictonarY: ",ke_values)

ke_values=ke_val_lis(keys,values)

print("the resultin list  is : ",ke_values)