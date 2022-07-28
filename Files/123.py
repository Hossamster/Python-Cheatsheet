""" Genertors """
""" generator is iterator but not iterator is generator  """
def count_up(max):
    count = 1
    while count <= max:
        yield count
        count += 1
counter = (count_up(10))
# print(counter)  
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# print(next(counter))
# print(next(counter))
# print("\n")
# for num in counter :
    # print(num)


'''
days = week()
next(days) # 'Monday'
next(days) # 'Tuesday'
next(days) # 'Wednesday'
next(days) # 'Thursday'
next(days) # 'Friday'
next(days) # 'Saturday'
next(days) # 'Sunday'
next(days) # StopIteration
'''

def week():
    lst = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
    for i in lst:
        yield i
days = week()
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))


'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''

def yes_or_no():
    lst = ['yes','no']
    while True:
        yield lst[0]
        yield lst[1]
k = yes_or_no()
# print(k)
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))

def current_peak():
    lst = [1,2,3,4]
    i = 0
    while True:
        if i >= len(lst):i=0
        yield lst[i]
        i += 1

counter = current_peak()
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))



'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''

def make_song(num,word):
    while num >= 0:
        if num == 1:
            yield f"Only {num} bottle of {word} left!"
        elif num == 0:
            yield f"No more {word}"
        else:
            yield f"{num} bottles of {word} on the wall" 
        num -= 1
kombucha_song = make_song(5, "kombucha")
# print(next(kombucha_song) )
# print(next(kombucha_song) )
# print(next(kombucha_song) )
# print(next(kombucha_song) )
# print(next(kombucha_song) )
# print(next(kombucha_song) )
# print(next(kombucha_song) )


