'''
Created on Mar 2, 2015

@author: kostadin
'''
import unittest
from big_game.extract_statistics import player_statistics
from big_game.extract_statistics import team_statistics
from big_game.extract_statistics import extract_game_passes
from big_game.extract_statistics import extract_game_motifs
from big_game.extract_statistics import extract_double_passes

class Test(unittest.TestCase):


    def testPlayerStat(self):
        pass
        g = player_statistics('../../Resources/BigGame/Data/vistrack-player-stats-130375.xml')
        self.assertEqual(g.ix[3]['name'], 'Florian Dick', "player statistics problem")
    
    
    def testTeamStat(self):
        pass
        g = team_statistics('../../Resources/BigGame/Data/vistrack-team-stats-130375.xml')
        self.assertEqual(g.ix[3]['fouls_commited'], 10, "team statistics problem")
        
    
    def testMotifsStat(self):
         passes = extract_game_passes('../../Resources/BigGame/Data/vistrack-actions-130375.xml')
         motifs_team1, motifs_team2 = extract_game_motifs(['O_9', 'O_44'], passes)
         self.assertEqual(motifs_team1[3], 'ABCD', "problem with motifs team 1")
#          print motifs_team1
#          print "===================================================================================="
#          print motifs_team2
         self.assertEqual(motifs_team2[5], 'ABAD', "problem with motifs team 2 " + motifs_team1[5])
         
    def testDoublePassStat(self):
        double_team1, double_team2 = extract_double_passes('../../Resources/BigGame/Data/vistrack-actions-130375.xml', ['O_9', 'O_44'])
#         print double_team1
#         print "===================================================================================="
#         print double_team2
        self.assertEqual(double_team1[1], 5, "double passes problem team 1")
        self.assertEqual(double_team2[3], 2, "double passes problem team 2")
        
         
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPlayerStat']
    unittest.main()