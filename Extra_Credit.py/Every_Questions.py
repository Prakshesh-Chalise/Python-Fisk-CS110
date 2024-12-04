# Q-2

# def non_repeat(input_list):
#     input_dictionary = {}
#     for elements in input_list:
#         if elements in input_dictionary:
#             input_dictionary[elements] = input_dictionary[elements] + 1
#         else:
#             input_dictionary[elements] = 1
#     for items in input_list:
#         if input_dictionary[items] == 1:
#             return items


#Q4

# def same_order(string_1,string_2):
#   word = ""
#   if len(string_2) == 0:
#     return True
#   pointer = 0
#   for char in string_1:
#     if string_2[pointer] == char:
#       pointer += 1
#     if pointer == len(string_2):
#       return True
#   return False

# print(same_order("abcPcbrakfdshesjh","Prakshesh"))




# Q6
# def flights(input_list):

#     new_dictionary = {}
#     new_list = []

#     for items in input_list:
#         new_dictionary[items[0]] = items[1]

#     values_list = new_dictionary.values()
#     keys_list = new_dictionary.keys()
#     departure  = set(keys_list)-set(values_list)
#     arrival = set(values_list) - set(keys_list)

#     if len(departure) > 1 or len(arrival) > 1:
#         return []

#     departure = list(departure)[0]
#     new_list.append(departure)
    

#     while departure in new_dictionary:
#          pointer = new_dictionary[departure]
#          new_list.append(pointer)
#          departure = pointer

#     return new_list


# Q7
# def reverse_vowels(input_string):

#     vowels = ['a', 'e', 'i', 'o', 'u']
#     new_list = []
#     reverse_list = []
#     word = ''
#     index = 0

#     for char in input_string:
#         if char.lower() in vowels:
#             new_list.append(char)

#     length = len(new_list)
#     for x in range(length-1,-1,-1):
#         reverse_list.append(new_list[x])

#     for char in input_string:
#         if char.lower() in vowels:
#             word = word + reverse_list[index]
#             index += 1
#         else:
#             word = word + char

#     return word





# Q3-Pair_sum_of_string

# def pair_sum_of_string_values(input_list,unique_int):
#     for items_1 in input_list:
#         for items_2 in input_list:
#             if items_1 + items_2 == unique_int:
#                 return (items_1, items_2)
#     return None







# Q5 - Diagonal_sum_of_string


# def diagonal_sum_of_string(input_list):
#     sum_of_string_1 = 0  
#     sum_of_string_2 = 0 
#     n = len(input_list) 

#     for i in range(n):
#         sum_of_string_1 += input_list[i][i]  
#         sum_of_string_2 += input_list[i][n - 1 - i]  

#     return (sum_of_string_1, sum_of_string_2)


# Q-10:

# def consecutive_number_strings(num_1, num_2):
#     string = ""
#     if num_2 > num_1:
#         for x in range(num_1, num_2 + 1):
#             string += str(x)
#     elif num_1 > num_2:
#         for x in range(num_1, num_2 - 1, -1):
#             string += str(x)
#     else:
#         return str(num_1)
#     return string


# Q9 - coinstar

# def coinstar(input_string):
 
#     sum_of_string = 0

#     for char in input_string:

#         char = char.lower()
   
#         if char == "p":
#             sum_of_string += 1e-2
        
#         elif char == "n":
#              sum_of_string += 5e-2
        
#         elif char == "d":
#              sum_of_string += 10e-2
        
#         elif char == "q":
#              sum_of_string += 25e-2
        
#         else:
#             return -1
        
#     sum_of_string = round(sum_of_string, 2)

#     return sum_of_string


# # Question_No_8:

# def greatest_sum_neighbors(input_list):

#     length = len(input_list)
#     highest_sum = 0
#     required_tuple = ()
#     for i in range(length):
    
#         for j in range(len(input_list[i])):
#             sum = 0
#             if i - 1 > -1:
#              sum += input_list[i-1][j] 

#             if j - 1 > -1:
#              sum += input_list[i][j-1]

#             if i - 1 > -1 and j-1 > -1:
#                sum += input_list[i-1][j-1]

#             if i + 1 < length:
#              sum += input_list[i+1][j]

#             if j + 1 < len(input_list[i]):
#              sum += input_list[i][j+1]

#             if i + 1 < length and j + 1 < len(input_list[i]):
#                sum += input_list[i+1][j+1]

#             if i + 1 < length and j - 1 > -1:
#               sum += input_list[i+1][j-1]

#             if i - 1 > -1 and j + 1 < len(input_list[i]):
#               sum += input_list[i-1][j+1]
            
#             if sum >= highest_sum:
#               highest_sum = sum
#               required_tuple = (i,j)
    
#     return required_tuple
              
                

        
# # Q1

# def update_plural(input_list):
#     count = 0

#     for x in range(len(input_list)):
#         items = input_list[x]
#         if len(items) > 0 and items[-1].lower() == "s":
#             item = items[0:-1:1]
#             input_list[x] = item
#             count += 1

#     return count
        
    



    






    



    



