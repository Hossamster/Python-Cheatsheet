sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
sounds.append("ayhaga")
print(sounds)
sounds.extend(['lol','ayhaga'])
print(sounds)
sounds.insert(1,'elberns')
print(sounds)
# sounds.clear()
# print(sounds)
sounds.pop(1)
print(sounds)
sounds.remove("ayhaga")
print(sounds)

print(sounds.index("ali",5,10))

sounds.reverse()
print(sounds)

sounds.sort()
print(sounds)

names = ['Mr',"Hossam"]
print(".".join(names))