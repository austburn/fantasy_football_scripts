import requests
from bs4 import BeautifulSoup


def format_player(row):
    link = row.find('td')
    try:
        href = link.find('a').get('href')
    except Exception:
        href = ''
    player_name = link.text.split(' ')

    cols = row.find_all('td')
    overall = cols[0].text.split(' ')[0][:-1]
    position = cols[0].text.split(' ')[-1]
    team = cols[1].text
    bye = cols[2].text
    rank = cols[3].text

    return "{overall},{last_name},{first_name},{position},{position_rank},{team},{bye},{link}".format(
        overall=overall,
        last_name=player_name[1],
        first_name=player_name[0],
        position=position,
        position_rank=rank,
        team=team,
        bye=bye,
        link=href)

# https://docs.google.com/spreadsheets/d/1yJLic0-KQnl9jIvFE0pc1O-O4ZsLMUnTYHvjd6M9JcA/edit?usp=sharing
if __name__ == '__main__':
    espn = requests.get('http://www.espn.com/fantasy/football/story/_/id/16287927/2016-fantasy-football-rankings-fantasy-football-player-rankings-top-fantasy-football-players-fantasy-football-draft')
    content = espn.text

    soup = BeautifulSoup(content, "html.parser")
    table = soup.find_all('tbody')[-1]
    players = table.find_all('tr')

    assert len(players) == 300

    f = open('espn.csv', 'w')
    f.write('OVERALL,LAST_NAME,FIRST_NAME,POSITION,POSITION_RANK,TEAM,BYE,LINK\n')

    for player in players:
        f.write(format_player(player))
        f.write('\n')

    f.close()
