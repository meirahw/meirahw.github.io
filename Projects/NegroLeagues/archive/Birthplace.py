import geocoder

def statesCodes():
    us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
    }
    
    # invert the dictionary
    abbrev_to_us_state = dict(map(reversed, us_state_to_abbrev.items()))

    return abbrev_to_us_state


def birthplace(soup, name, full_player_url, player_dict, unknown_dict):

    birthplace = ''
    
    for span in soup.find_all('span'):
        
        txt = span.text.strip()
        
        if "in " in txt:

            birthplace = txt.split('in ')[1]

            abbrev_to_us_state = statesCodes()

            for abbrev in abbrev_to_us_state:
                
                if abbrev in birthplace:
            
                    birthplace = birthplace.replace(abbrev, abbrev_to_us_state[abbrev])

            break;
    
    try:
    
        location = geocoder.mapquest(birthplace, key='LfWPHDU58EB4CdDtyHKSO91NHbIEe4bW')
            
        player_dict[name] = {'place': birthplace, 'coords': location.latlng, 
                             'player_url': full_player_url,} #'team_url': team_url}

        # print(name + " was born in " + birthplace)

    except:

        # print(name + " has an unknown birthplace")

        unknown_dict[name] = {'place': birthplace, 'coords': [None, None], 
                       'url': full_player_url,} #'team_url': team_url}

    return player_dict