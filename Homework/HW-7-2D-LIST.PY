# def greatest_row_sum(my_list):

#     length = len(my_list)

#     row = 0
#     column = 0
#     row_total = 0

#     for x in range(length):
#        length_of_individual_row = 0
#        for length_of_individual_row in range(1):
#           length_of_individual_row = length_of_individual_row + 1
          

#     store_value = 0

#     if length < 0 or length_of_individual_row < 0:
       
#        return []


#     else:

#      for row in range(length):

#         row_total = 0

#         for column in range(length_of_individual_row + 1):
#            element = my_list[row][column]
#            row_total = row_total + element

#         if row_total > store_value:
#             store_value = row_total

#         else:
#             store_value = store_value
    
#      return store_value
    



# print(greatest_row_sum([[],[],[2]]))

def greatest_row_sum(my_list):
     
   length = len(my_list)

   if length == 0 or (length == 1 and not my_list[0]):
    return None
   
   else:
    
    for row in range(length):
       row_total = 0
       row_value = 0
       for column in range(len(my_list[row])):
          row_value = my_list[row][column]
          row_total = row_total + row_value

       if row == 0:
              store_value = row_total

       if row_total >= store_value:
            store_value = row_total

       else:
            store_value = store_value
   
    return store_value
   



print(greatest_row_sum([]))





    



    