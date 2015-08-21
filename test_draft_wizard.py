import unittest
from bs4 import BeautifulSoup

from ffb.draft_wizard import format_player


class TestPlayer(unittest.TestCase):
    def test_player_format(self):
        row = BeautifulSoup('<tr class="PosRB"> \
                                <td>RB1</td>\
                                <td>1</td>\
                                <td class="playerName">\
                                    <a href="http://www.fantasypros.com/nfl/players/leveon-bell.php" target="_blank">Le\'Veon Bell</a>\
                                </td>\
                                <td>PIT  <span class="ByeWeek" title="Bye Week">(11)</span></td>\
                                <td>1.01</td>\
                                <td>1.01</td>\
                                <td>1.05</td>\
                                <td>0.53</td>\
                                <td>100%</td>\
                            </tr>')

        self.assertEqual('1,Bell,Le\'Veon,RB,RB1,PIT,11,1.01,1.01,1.05,0.53,100%,http://www.fantasypros.com/nfl/players/leveon-bell.php', format_player(row))
