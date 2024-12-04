# def construct_2D(i_list,m,n):

#     length = len(i_list)
#     main_list = []
#     x = 0
#     y = 0

#     if m * n != length:
#         return []
    
#     else:
#         while  x < length:
#             sub_list = []

#             for _ in range(n):
#                 value = i_list[x]
#                 sub_list.append(value)
#                 x += 1
            
#             main_list.append(sub_list)

#     return main_list


# def count_matches(i_list,ruleKey,ruleValue):
#     count = 0
#     length = len(i_list)
#     for x in range(length):
#         if ruleKey == "type" and i_list[x][0] ==  ruleValue:
#             count += 1
#         elif ruleKey == "color" and i_list[x][1] ==  ruleValue:
#             count += 1
#         elif ruleKey == "name" and i_list[x][2] ==  ruleValue:
#             count += 1
#     return count
