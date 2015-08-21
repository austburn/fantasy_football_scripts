import unittest
from bs4 import BeautifulSoup

from ffb.espn import format_player


class TestPlayer(unittest.TestCase):
    def test_player_format(self):
        row = BeautifulSoup('<tr class="last"><td>1. <a href="http://espn.go.com/nfl/player/_/id/15825/le\'veon-bell">Le\'Veon Bell</a>, RB</td><td>PIT</td><td>11</td><td>RB1</td><td>$55</td></tr>')

        self.assertEqual('1,Bell,Le\'Veon,RB,RB1,PIT,11,http://espn.go.com/nfl/player/_/id/15825/le\'veon-bell', format_player(row))
