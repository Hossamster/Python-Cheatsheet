temp = []
    for x in my_list:
        if x < 0:
            temp.append(abs(x))
        else:
            temp.append(x)