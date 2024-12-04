
def common_first_letters(input_list):


    new_dictionary = {}

    for strings in input_list:
       
       keyword = strings[0].lower()

       if keyword in new_dictionary:
          new_dictionary[keyword] = new_dictionary[keyword] + 1

       else:
          new_dictionary[keyword] = 1
    
    count = 0

    for keys in new_dictionary:
       
       if new_dictionary[keys] >= 2:
          count = count + 1
    
    return count


print(common_first_letters(["Ball", "boo", "*", "*", 'This', 'tis', 'is', 'an', 'interesting', 'problem','that', "8", "8"]))