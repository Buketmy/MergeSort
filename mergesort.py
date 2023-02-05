string_data:str = "5 7 2 9 6 1 3 8"
split_list1:list = string_data.split(" ")[0:4]
split_list2:list = string_data.split(" ")[4:8]
print(split_list1,split_list2)

# içine ['2','3','4'] tarzında liste alır
def str_list_sort(str_list:list) -> list:
    my_temp_list:list =[] 
    for i in str_list: 
        my_temp_list.append(int(i))
    my_temp_list.sort()
    return my_temp_list
    
siralama1 = str_list_sort(split_list1)
siralama2 = str_list_sort(split_list2)
print(siralama1, siralama2)

birlesim:str = siralama1 + siralama2
print(birlesim)

sonsiralama:str = str_list_sort(birlesim)
print(sonsiralama)
