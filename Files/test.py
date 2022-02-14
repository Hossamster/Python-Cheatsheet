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

my_songs = map(lambda x:x['song'],playlist)
print(tuple(my_songs))
