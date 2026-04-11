import time
from Birthplace import birthplace
from UrlRequest import urlRequestSoup, urlRequestTable
import json
from Teams import variables


def openTxtFile(file):
        
    url_txt = open("negroLeague" + file + "_urls.txt", 'r')

    for url in url_txt:
        
        url_list = url.split(", ")
    
    url_list = [url for url in url_list if url]
    
    return url_list

team_url_list = openTxtFile("Teams")

def get_data(team_url_list):

    player_dict = {}
    unknown_dict = {}
    player_urls = []
    base_url = variables()[0]   
    mlp = "Major League Players"
    
    for team in team_url_list: 
        
        table = urlRequestTable(team, variables()[2])

        time.sleep(2)
        
        for row in table:

            player_url = row.get("href")
            full_player_url = base_url + player_url

            # ignore Major League Players and hope they always stay at the bottom?
            if mlp in row:

                break;
            
            if full_player_url not in player_urls:
               
                player_urls.append(full_player_url)
                soup = urlRequestSoup(full_player_url)
                                      
                name = row.contents[0]
        
                player_birthplace_dict = birthplace(soup, name, full_player_url, player_dict, unknown_dict)
                
                continue        
        
        # continue to next org/year after hitting (current) Major League Players       
        
        continue

    return player_birthplace_dict

player_birthplace_dict = get_data(team_url_list)

# write to json
json_object = json.dumps(player_birthplace_dict, indent=4)

with open("player_birthplace.json", "w") as outfile:
    outfile.write(json_object)