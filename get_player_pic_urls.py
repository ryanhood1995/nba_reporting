#
# Author: Ryan Hood
# Date: 5/21/2022
#
# Description: This script ..


import pandas as pd
from urllib.request import urlopen
import json




EARLIEST_LOOKBACK_YEAR = 2012 #2012 is the earliest year that works with this method.
LATEST_LOOKBACK_YEAR = 2021


# Create empty dataframe to load values in.
result_df = pd.DataFrame(columns=['player_name', 'season', 'url'])

# Loop through each year from earliest to latest.
current_lookback_year = EARLIEST_LOOKBACK_YEAR
while current_lookback_year <= LATEST_LOOKBACK_YEAR:
    
    json_url = "https://data.nba.net/data/10s/prod/v1/{}/players.json".format(str(current_lookback_year))
    
    response = urlopen(json_url)

    data_json = json.loads(response.read())
    
    # print the json response
    players_list = data_json['league']['standard']
    
    for player in players_list:
        
        player_full_name = player['firstName'] + ' ' + player['lastName']
        player_id = player['personId']
        
        url = "https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/{}.png".format(str(player_id))
        
        new_entry = {'player_name': player_full_name, 'season': current_lookback_year, 'url': url}
        
        result_df = result_df.append(new_entry, ignore_index = True)
        
        continue

    
    current_lookback_year = current_lookback_year + 1
    continue


# Save the dataframe as csv file.
result_df.to_csv('player_pic_urls.csv')



