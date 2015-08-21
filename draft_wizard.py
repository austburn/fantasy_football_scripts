import requests
from bs4 import BeautifulSoup
import re


def format_player(row):
    link = row.find('a')
    href = link.get('href')
    player_name = link.text.split(' ')

    cols = row.find_all('td')
    position_rank = cols[0].text
    position_match = re.search('([A-Z]{1,3})\d{0,3}', position_rank)
    position = position_match.groups()[0]

    overall = cols[1].text

    team_and_bye = cols[3].text
    team_and_bye_match = re.search('(\w{2,3})\s{0,3}\((\d{1,2})\)', team_and_bye)

    try:
        team = team_and_bye_match.groups()[0]
        bye = team_and_bye_match.groups()[1]
    except:
        team = 'FA'
        bye = 'FA'

    avg_pick = cols[4].text
    high = cols[5].text
    low = cols[6].text
    std_dev = cols[7].text
    percent_drafted = cols[8].text

    return "{overall},{last_name},{first_name},{position},{position_rank},{team},{bye},{avg_pick},{high},{low},{std_dev},{percent_drafted},{link}".format(
        overall=overall,
        last_name=player_name[1],
        first_name=player_name[0],
        position=position,
        position_rank=position_rank,
        team=team,
        bye=bye,
        avg_pick=avg_pick,
        high=high,
        low=low,
        std_dev=std_dev,
        percent_drafted=percent_drafted,
        link=href)


if __name__ == '__main__':
    dw = requests.get('http://draftwizard.fantasypros.com/nfl/adp/mock-drafts/overall/default-ppr-14-teams')
    content = dw.text

    soup = BeautifulSoup(content)
    table = soup.find('tbody')
    players = table.find_all('tr')

    f = open('dw.csv', 'w')
    f.write('OVERALL,LAST_NAME,FIRST_NAME,POSITION,POSITION_RANK,TEAM,BYE,AVG_PICK,HIGH,LOW,STD_DEV,PERCENT_DRAFTED,LINK\n')

    for player in players:
        f.write(format_player(player))
        f.write('\n')

    f.close()
