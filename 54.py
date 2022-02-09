nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
just = [[print(val) for val in range(4)] for ayhaga in nested_list]
print(just)

# board = [[col for col in range(1,4)] for row in range(1,5)]
# print(board)

# lol = [['x' if num % 2 == 0 else 'o' for num in range(1,4)] for row in range (1,6)]
# print(lol)

# answer = [[col for col in range(0,10)] for row in range(1,11)]
# print(answer)