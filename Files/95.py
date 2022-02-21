#handling error
#try and except
try:
    hossam
except:
    print("u tried hossam walahi bas mafish ay haga 5ales")
#u tried hossam walahi bas mafish ay haga 5ales


# d = {"name":"Rick"}
# d['city'] >> keyerror

def get(key):
    try:
        # if type(key) == list:
        #     raise TypeError("Maynfa3sh list tkon as a key in the dictionary")
        return d[key]
    except KeyError:
        return f"kan nefsi arga3 walahi"
d = {"name":"Rick"}
print(get('name'))  # rick 
print(get('names')) # kan nefsi arga3 walahi