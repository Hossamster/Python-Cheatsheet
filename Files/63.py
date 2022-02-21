#data modeling using lists and dictionary
# spotify playlist
playlist = {
    'title' : "Hossam's playlist",
    'author':"Hossam",
    'songs':[
        {'title':'2oly 2al','artist':["Ahmed Kamel"],'duration':2.5},
        {'title':'hay3efsh tftkrny','artist':["Amr Diab"],'duration':4},
        {'title':'atemn','artist':["Tamer Hosny","Aliaa"],'duration':5.3},
        {'title':'meshwar tawil','artist':["Ahmed Fahmy",'Nader Hamdy','Mohamed Nour'],'duration':1.4}
    ]
}
total_length = 0
for song in playlist['songs']:
    print(song['artist'],song['title'])
    total_length += song.get('duration')
print(total_length)

print("\n")

for i in playlist['songs']:
    if i['title'] == 'atemn':
        print(i['artist'])

"""
you can not use list as a key in dictionary 
"""