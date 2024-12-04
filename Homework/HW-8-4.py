# You may use a set and/or a dictionary to solve this problem. Do not create any other data structures. 

# You should not mutate the contents of the list passed to your function.


# def odd_occurrences(list_1):

#   if len(list_1) == 0:
#     return set()
  
#   else:

#     empty_set = {}

#     for elements in list_1:

#         if elements in empty_set:

#          empty_set[elements] += 1

#         else:
         
#          empty_set[elements] = 1
     
    
#     empty_set_2 = set()


#     for keys in empty_set:
 
#          if empty_set[keys] % 2 != 0:

#             empty_set_2.add(keys)
        
#     if len(empty_set_2) == 0:

#         return set()
    
#     else:
#         return empty_set_2


# print(odd_occurrences([4, 1, 2, 1, 2, 2]))

def odd_occurrences(list_1):

    if not list_1:
        return set()

    count_dict = {}

    for element in list_1:
        count_dict[element] = count_dict.get(element, 0) + 1

    return {key for key, value in count_dict.items() if value % 2 != 0}

print(odd_occurrences([4, 1, 2, 1, 2, 2]))


    
  