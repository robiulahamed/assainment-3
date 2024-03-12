list_of_tuples = [(2,500),(10,100),(20,400),(50,200),(40,300)]

 
sorted_list = sorted(list_of_tuples, key=lambda x: x[1])


print("Sorted List of Tuples based on the second element:")
print(sorted_list)