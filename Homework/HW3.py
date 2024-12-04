string_1 = input("String 1 please? ")
string_2 = input("String 2 please? ")
length_string_1 = len(string_1)
length_string_2 = len(string_2)
concatenated_strings = ""

if length_string_1 >= length_string_2:
    
    for x in range(length_string_1):

        alternate_1 = string_1[x]

        concatenated_strings = concatenated_strings + alternate_1

        if x < (length_string_2):
           
           alternate_2 = string_2[x]

           concatenated_strings = concatenated_strings + alternate_2
           

else:

    for x in range(length_string_2):

      if x < (length_string_1):

        alternate_1 = string_1[x]

        concatenated_strings = concatenated_strings + alternate_1

      alternate_2 = string_2[x]

      concatenated_strings = concatenated_strings + alternate_2

    
print(concatenated_strings)