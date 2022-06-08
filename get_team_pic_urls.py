#
# Author: Ryan Hood
# Date: 5/22/2022
#
# Description: This script ..

import pandas as pd

TEAMS = ['atl',
  'bkn',
  'bos',
  'cha',
  'chi',
  'cle',
  'dal',
  'den',
  'det',
  'gsw',
  'hou',
  'ind',
  'lac',
  'lal',
  'mem',
  'mia',
  'mil',
  'min',
  'nop',
  'nyk',
  'okc',
  'orl',
  'phi',
  'phx',
  'por',
  'sac',
  'sas',
  'tor',
  'uta',
  'was']


TEAMS_LONG = ['Hawks',
              'Nets',
              'Celtics',
              'Hornets',
              'Bulls',
              'Cavaliers',
              'Mavericks',
              'Nuggets',
              'Pistons',
              'Warriors',
              'Rockets',
              'Pacers',
              'Clippers',
              'Lakers',
              'Grizzlies',
              'Heat',
              'Bucks',
              'Timberwolves',
              'Pelicans',
              'Knicks',
              'Thunder',
              'Magic',
              '76ers',
              'Suns',
              'Trailblazers',
              'Kings',
              'Spurs',
              'Raptors',
              'Jazz',
              'Wizards'
    ]



result_df = pd.DataFrame(columns=['nickname', 'url'])


for team_index in range(0, len(TEAMS)):
    
    team_abbr = TEAMS[team_index]
    nickname = TEAMS_LONG[team_index]
    
    url = 'https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/{}.png'.format(team_abbr)
    
    new_entry = {'nickname': nickname, 'url': url}
    
    result_df = result_df.append(new_entry, ignore_index = True)
    
    continue


# Save the dataframe as csv file.
result_df.to_csv('team_pic_urls.csv')









