
# def product(a,b):
#     multiplication = (a * b)
#     result = "'" + str(multiplication) + "'"
#     return result

# print(product(-2,-3))

def product_range(number, beginning, end):
    product_table = ""
    if end > beginning:

        for x in range(beginning, (end + 1)):

            multiplied = number * x

            product_table += str(multiplied) + "\t"

        return product_table

    else:
        return ""
    
    
print(product_range(2, 5, 8))


# def product_square(first_number, second_number, third_number, fourth_number):

#     line   = ""

#     for x in range(first_number, second_number + 1):

#         result = ""

#         for y in range(third_number, fourth_number + 1):

#             product = x * y

#             result = result + str(product) + "\t"

#         line = line + result + "\n"

#     return line

# print(product_square(3, 5, 2, 5))



    
