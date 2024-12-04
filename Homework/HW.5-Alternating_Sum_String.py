number = input()
length = len(number)
new_even = 0
new_odd = 0
for x in range(1, (length)):
    if x % 2 == 0:
        new_even = int(number[x])+new_even
    else:
        new_odd = int(number[x])+ new_odd
new = -(new_even) + new_odd
new = int(number[0]) + new
print(new)
