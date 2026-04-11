import folium
import json

def JSONtoDict(json_file):
    
    f = open(json_file)
    dict_ = json.load(f)
    f.close()

    return dict_

dict_players = JSONtoDict("player_birthplace.json")

m = folium.Map(location=[48, -102], zoom_start=3)

# add marker one by one on the map
for name in dict_players:
    
    coords = dict_players[name]['coords']
    place = dict_players[name]['place']
    url = dict_players[name]['player_url']

    if coords != None:

        lat = coords[0]
        lon = coords[1]
    
        folium.Marker(location=[lat, lon], popup = (name,place,url)).add_to(m)

# Show the map
m

for name in dict_players:
    place = dict_players[name]['place']
    if "," not in place:
        print(name, place)