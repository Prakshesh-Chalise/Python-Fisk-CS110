def clean_list(my_list):
    x = 0
    length = len(my_list)
    while x < length:
        if my_list[x] == 0:
            my_list.pop(x)
            length = length - 1
            x = x - 1
        x = x + 1
    return my_list

print(clean_list([1,2,3,4,5]))