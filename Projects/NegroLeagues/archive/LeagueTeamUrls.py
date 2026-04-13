import requests, time
from UrlRequest import urlRequestTable

def negroLeaguesTeams(base_url, leagues_s, teams_s, shtml, league_ls, year_ls, anl_url, nsl_url, ewl_url):
    
    league_url_ls = []
    team_url_ls = []
    
    # get list of all league urls
    for league in league_ls:

        for year in year_ls:
           
            # create full url
            league_url_full = base_url + leagues_s + league + r"/" + year + shtml
            
            # check to see if url exists and don't get banned again lol
            r = requests.get(league_url_full)
            time.sleep(2)

            # add non broken pages to list
            if r.status_code != 404:
                league_url_ls.append(league_url_full)

                print("Gathering " + year + " " + league)
    
    league_url_ls.extend((anl_url, nsl_url, ewl_url))
                         
    # get list of all team urls
    for league_url in league_url_ls:
        
        # get web page where list of teams exists
        table = urlRequestTable(league_url, teams_s)

        for row in table:

            if not "Major League Teams" in row:
               
                team_url = row.get("href")
                full_team_url = base_url + team_url

                if full_team_url not in team_url_ls:
                
                    team_url_ls.append(full_team_url)
    
                    print("Gathering " + team_url[-12:-5])
                
            # exit loop after hitting Major League Teams
            else:
                
                break;
        
    return league_url_ls, team_url_ls