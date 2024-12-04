def merge_lists(a, b):
    length_a = len(a)
    length_b = len(b)
    new_list = []
    
    x = 0
    y = 0
    
    while x < length_a and y < length_b:
        element_a = a[x]
        element_b = b[y]
        
        if element_a < element_b:
            new_list.append(element_a)
            x = x + 1

        elif element_a == element_b:
            new_list.append(element_a)
            new_list.append(element_b)
            x = x + 1
            y = y + 1

        else:
            new_list.append(element_b)
            y = y + 1
    
    while x < length_a:
        new_list.append(a[x])
        x = x + 1

    while y < length_b:
        new_list.append(b[y])
        y = y + 1

    return new_list

print(merge_lists([], [1]))


# def merge_lists(a, b):
#     length_a = len(a)
#     length_b = len(b)
#     new_list = []
    
#     x = 0
#     y = 0
    

#     while x < length_a and y < length_b:
#         element_a = a[x]
#         element_b = b[y]
        
#         if element_a < element_b:
#             new_list.append(element_a)
#             x += 1
#         elif element_a == element_b:
#             new_list.append(element_a)
#             new_list.append(element_b)
#             x += 1
#             y += 1
#         else:
#             new_list.append(element_b)
#             y += 1
    
#     while x < length_a:
#         new_list.append(a[x])
#         x += 1

#     while y < length_b:
#         new_list.append(b[y])
#         y += 1

#     return new_list

# print(merge_lists([3, 6, 6, 9, 11], [5, 6, 7]))

            
            
            