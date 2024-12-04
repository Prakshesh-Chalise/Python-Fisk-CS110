first_string = int(input())
second_string = int(input())
new_string = ""
if first_string > second_string:
    for x in range(first_string, (second_string-1), -1):
        new_string = new_string + str(x)
    print(new_string)

elif second_string > first_string:
    for x in range(first_string, (second_string)+1):
        new_string = new_string + str(x)
    print(new_string)
else:
    print(first_string)
                   

