# def most_frequent_element(i_list):

#     new_dictionary = dict()

#     for element in i_list:
#         if element in new_dictionary:
#             new_dictionary[element] += 1
#         else:
#             new_dictionary[element] = 1
    
#     values = list(new_dictionary.values())
#     initializer = values[0]

#     for x in range(1, len(values)):
#         if values[x] >= initializer:
#             initializer = values[x]
    
#     for elements in new_dictionary:
#         if new_dictionary[elements] == initializer:
#             return elements


# def word_count(input_string):

#     length = len(input_string)
#     x = 0
#     new_dict = {}
    
#     while x < length:
#         word = ""
#         while x < length:
#             if input_string[x] != " ":
#              word += input_string[x]
#              x += 1
#             else:
#                 break
        
#         if word in new_dict:
#             new_dict[word] += 1
#         else:
#             new_dict[word] = 1
        
#         x += 1

#     return new_dict

# result = word_count("That that is is that that is not is not Is that it It is")
# print(result)
    
        

  

