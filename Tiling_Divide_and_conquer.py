from random import randint
n = int(input("enter"))
arr = [[ 0 for col in range(n)]for row in range(n) ]
print(arr)
temp = int((n-1)//2) # 3
tempp = int((n/2)+1) # 5

#base case
def board_size_is_2(x,y):
    rand = randint(0,n)
    print(rand)
    for i in range(0,n):
        for j in  range(0,n):
            if arr[i][j] != arr[x][y]:
                arr[i][j] = rand
    print(arr)

def tile_the_center(x,y):
    rand = randint(0,n)
    print(rand)
    
    for i in range(temp,tempp): # 3 , 5
        for j in  range(temp,tempp): # 3 , 5 
            if arr[i][j] != arr[x][y]:
                arr[i][j] = rand
    if (x != temp and y != tempp-1) or (x != temp and y != temp) or (x != tempp - 1 and y != temp) or (x != tempp - 1 and y != tempp - 1):
        arr[temp][temp] = 0
    print(arr)




# def tile_the_other_3(x,y):

#     for i in range(temp,tempp):
#         for j in range(temp,tempp):
#             # "D"
#             if arr[x][y] == arr[i][j]:
#                 tile_the_center(x,y)


def def_square_loc(x,y):
    s = int(n/2)
    arr[x][y] = 'D'
    print(arr)
    if x > n or y > n:
        raise ValueError("x and y values must be equal to n")
    if n == 1: 
        return "can't be tiled"
    elif n % 2 != 0 :
        return "Please enter even number"
    elif n == 2:
        board_size_is_2(x,y)
    elif n > 2:
        # if the defective square near the center then tile the other 3 quadrants
        tile_the_center(x,y)
        
def_square_loc(6,6)