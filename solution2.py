def mult_list(my_list):
    result = 1
    for i in range(0, len(my_list)):
        result = result * my_list[i]
    return result

list1= [2,5,3]
list2= [1,3,7]
print(mult_list(list1))
print(mult_list(list2))
