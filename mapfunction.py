def cel_to_far(temperatur):
    return (temperatur*9/5)+32


cel_tem=[20,30,35,40]
far_tem=list(map(cel_to_far, cel_tem))

print("the celcusss temperatur : ", cel_tem)
print("the farrenhte tempreature :",far_tem)