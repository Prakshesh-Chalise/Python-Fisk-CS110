
def rle_decompress(my_list):

    new_list = []

    length = len(my_list)

    value_index = 0

    if length > 0:

     while value_index < length:
         
         appending_count = 0
         
         while appending_count < my_list[value_index + 1]:

           appending_value = my_list[value_index]

           new_list.append(appending_value)

           appending_count += 1

         value_index += 2

     return new_list

    else:

     return []



def rle_compress(my_list):
    new_list = []
    length = len(my_list)
    x = 0
  
    if length > 0:

     while x < length:

        y = 1

        while x + 1 < length and my_list[x] == my_list[x+1]:

            y = y + 1
            x = x + 1
    
        new_list.append(my_list[x])

        new_list.append(y)

        x = x + 1
    
     return new_list

    else:
    
     return []






