from operator import index
import pandas as pd 
from pathlib import Path

PRE_1970_DIVISIONS = '|'.join(["Coastal","Capitol", "Central", "Century", "American", "National", "East", "West"])
POST_1970_DIVISIONS = '|'.join(["AFC", "NFC"])

def get_files(dirname):
    standings_files = [(x, int(x.stem)) for x in Path(f'./{dirname}').iterdir()]
    return standings_files

def extract_pre1970(htmlfile, divisions_list):
    standings = pd.read_html(htmlfile, index_col=False)[0]
    standings = standings[standings['Tm'].str.contains(divisions_list) == False]
    standings['Tm'] = standings['Tm'].map(lambda x: x.rstrip("+*"))
    return standings.reset_index(drop=True)

def extract_merger(htmlfile):
    standings_afc = pd.read_html(htmlfile)[0]
    standings_nfc = pd.read_html(htmlfile)[1]
    standings_afc = standings_afc[standings_afc['Tm'].str.contains(POST_1970_DIVISIONS) == False]
    standings_nfc = standings_nfc[standings_nfc['Tm'].str.contains(POST_1970_DIVISIONS) == False]
    standings = pd.concat([standings_nfc, standings_afc], axis=0)
    standings['Tm'] = standings['Tm'].map(lambda x: x.rstrip("+*"))
    return standings.reset_index(drop=True)

def main():
    for x, y in get_files('nfl'):
        if y < 1970:
            data = extract_pre1970(x, PRE_1970_DIVISIONS)
            data.to_csv(Path('./csv') / f'{y}.csv')
        else:
            data = extract_merger(x)
            data.to_csv(Path('./csv') / f'{y}.csv')

    for x, y in get_files('afl'):
        data = extract_pre1970(x, PRE_1970_DIVISIONS)
        data.to_csv(Path('./csv') / f'{y}_afl.csv')

    for x, y in get_files('aafc'):
        data = extract_pre1970(x, PRE_1970_DIVISIONS)
        data.to_csv(Path('./csv') / f'{y}_aafc.csv')

    for x, y in get_files('apfa'):
        data = extract_pre1970(x, PRE_1970_DIVISIONS)
        data.to_csv(Path('./csv') / f'{y}_apfa.csv')

if __name__ == "__main__":
    main()
