import pandas as pd 
from pathlib import Path

MODERN_TEAM_NAMES = {"Chicago Cardinals": "Arizona Cardinals",
                     "St. Louis Cardinals": "Arizona Cardinals",
                     "Phoenix Cardinals": "Arizona Cardinals",
                     "Arizona Cardinals": "Arizona Cardinals",
                     "Atlanta Falcons": "Atlanta Falcons",
                     "Baltimore Ravens": "Baltimore Ravens",
                     "Buffalo Bills": "Buffalo Bills",
                     "Carolina Panthers": "Carolina Panthers",
                     "Decatur Staleys": "Chicago Bears",
                     "Chicago Staleys": "Chicago Bears",
                     "Chicago Bears": "Chicago Bears",
                     "Cincinnati Bengals": "Cincinatti Bengals",
                     "Cleveland Browns": "Cleveland Browns",
                     "Dallas Cowboys": "Dallas Cowboys",
                     "Denver Broncos": "Denver Broncos",
                     "Portsmouth Spartans": "Detroit Lions",
                     "Detroit Lions": "Detroit Lions",
                     "Green Bay Packers": "Green Bay Packers",
                     "Houston Texans": "Houston Texans",
                     "Baltimore Colts": "Indianapolis Colts",
                     "Indianapolis Colts": "Indianapolis Colts",
                     "Jacksonville Jaguars": "Jacksonville Jaguars",
                     "Dallas Texans": "Kansas City Chiefs",
                     "Kansas City Chiefs": "Kansas City Chiefs",
                     "Oakland Raiders": "Las Vegas Raiders",
                     "Los Angeles Raiders": "Las Vegas Raiders",
                     "Las Vegas Raiders": "Las Vegas Raiders",
                     "San Diego Chargers": "Los Angeles Chargers",
                     "Los Angeles Chargers": "Los Angeles Chargers",
                     "Cleveland Rams": "Los Angeles Rams",
                     "St. Louis Rams": "Los Angeles Rams",
                     "Los Angeles Rams": "Los Angeles Rams",
                     "Miami Dolphins": "Miami Dolphins",
                     "Minnesota Vikings": "Minnesota Vikings",
                     "Boston Patriots": "New England Patriots",
                     "New England Patriots": "New England Patriots",
                     "New Orleans Saints": "New Orleans Saints",
                     "New York Giants": "New York Giants",
                     "New York Titans": "New York Jets",
                     "New York Jets": "New York Jets",
                     "Philadelphia Eagles": "Philadelphia Eagles",
                     "Pittsburgh Pirates": "Pittsburgh Steelers",
                     "Pittsburgh Steelers": "Pittsburgh Steelers",
                     "San Francisco 49ers": "San Francisco 49ers",
                     "Seattle Seahawks": "Seattle Seahawks",
                     "Tampa Bay Buccaneers": "Tampa Bay Buccaneers",
                     "Houston Oilers": "Tennessee Titans",
                     "Tennessee Oilers": "Tennessee Titans",
                     "Tennessee Titans": "Tennessee Titans",
                     "Boston Braves": "Washington Commanders",
                     "Boston Redskins": "Washington Commanders",
                     "Washington Redskins": "Washington Commanders",
                     "Washington Football Team": "Washington Commanders",
                     "Washington Commanders": "Washington Commanders"}

def prepare_csv(csvfile, season, league):
    standings = pd.read_csv(csvfile)
    standings['season'] = season
    standings['league'] = league
    standings['modern_name'] = standings['Tm'].map(MODERN_TEAM_NAMES)
    return standings

def get_files():
    filelist = [[x] for x in Path('./csv').iterdir()]
    for x in filelist:
        y = x[0].stem.split('_')
        if len(y) > 1:
            x.append(int(y[0]))
            x.append(y[1])
        else:
            x.append(int(y[0]))
            x.append('nfl')
    return filelist

def main():
    all_standings = []
    filelist = get_files()
    for csvfile, season, league in filelist:
        all_standings.append(prepare_csv(csvfile, season, league))
    standings = pd.concat(all_standings, axis=0)
    standings = standings[['league', 'season', 'Tm', 'modern_name', 'W', 'L', 'T', 'W-L%', 'PF', 'PA', 'PD', 'MoV', 'SoS',
                          'SRS', 'OSRS', 'DSRS']]
    standings = standings.sort_values(by=['season', 'league'])
    standings = standings.reset_index(drop=True)
    standings.to_csv(Path('./combined_records.csv'), index=False)

if __name__ == "__main__":
    main()
