from LeagueTeamUrls import negroLeaguesTeams

def variables():

    base_url = "https://www.baseball-reference.com"
    leagues_s = "/leagues/"
    players_s = "/players/"
    teams_s = "/teams/"
    shtml = ".shtml"

    nnl = "NNL" #Negro National League
    nn2 = "NN2" #Negro National League II
    ecl = "ECL" #Eastern Colored League

    anl = "ANL" #American Negro League - 1929
    nsl = "NSL" #Negro Southern League - 1932
    ewl = "EWL" #East West League - 1932
    
    # comment out if this ever changes and see return
    anl_url = base_url + leagues_s + anl + r"/" + str(1929) + shtml 
    nsl_url = base_url + leagues_s + nsl + r"/" + str(1932) + shtml 
    ewl_url = base_url + leagues_s + ewl + r"/" + str(1929) + shtml 
    # -------------------------------------------------------
    
    start_date = 1920
    end_date = 1949 #+1 - real end date is 1948
    
    league_ls = [nnl, nn2, ecl] #, anl, nsl, ewl]
    
    year_ls = [str(year) for year in range(start_date, end_date)]
           
    return base_url, leagues_s, players_s, teams_s, shtml, league_ls, year_ls, anl_url, nsl_url, ewl_url # comment out anl_url, nsl_url, ewl_url

league, team = negroLeaguesTeams(variables()[0], variables()[1], variables()[3], variables()[4], variables()[5], variables()[6], variables()[7], variables()[8], variables()[9])

def saveTxtFile(file):

    urls = list(set(file))
    urls = [url for url in urls if url not in ["https://www.baseball-reference.com/teams/"]]

    f = open("negroLeague" + str(file) + '_urls.txt', 'w')
    
    for url in urls:
        print(url)
        f.write(url + ", ")
        
saveTxtFile(team)
        
def openTxtFile(file):
        
    url_txt = open("negroLeague" + file + "_urls.txt", 'r')

    for url in url_txt:
        
        url_list = url.split(", ")
    
    url_list = [url for url in url_list if url]
    
    return url_list

