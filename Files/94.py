# raise our own errors
def color(word,urcolor):
    colors = ("cyan",'yellow','blue','green','magenta','red')
    if type(word) != str:
        raise TypeError("5aly el word string ya haywan")
    if type(urcolor) != str:
        raise TypeError("5aly el color string ya haywan")
    if urcolor not in colors:
        raise  ValueError("E5tar color mn el colors ya haywan")
    print(f"printed {word} in {urcolor}")
color('hello','red')
# color('hello','nothing')
color('dsd',1)

