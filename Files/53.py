# nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#           col0  col1  col2
# row 0     [1,    2,    3]
# row 1     [4,    5,    6]
# row 2     [7,    8,    9]
# print(len(nested_list))

# accessing nested lists
print(nested_list[0][1])
print(nested_list[1][-1])
print(nested_list[-1][-2])

# for row in nested_list:
#     print(row)

# for row in nested_list:
#     for col in row:
#         print(col)


# [[print(col) for col in row] for row in nested_list]
