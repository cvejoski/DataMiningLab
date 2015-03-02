'''
Created on Mar 2, 2015

@author: kostadin
'''
import unittest
import numpy as np
import pandas as pd
from pandas import DataFrame
from small_game.running_performance import current_running_statistics

class Test(unittest.TestCase):


    def testCurrentRunningStat(self):
        pass
        arrayTeamA = np.array([np.array(['GKA', 13, 14, 97, 98]), 
                      np.array(['A1', 47, 16, 0, 0]),
                      np.array(['A2', 49, 88, 0, 0]),
                      np.array(['A3', 19, 52, 0, 0]),
                      np.array(['A4', 53, 54, 0, 0]),
                      np.array(['A5', 23, 24, 0, 0]),
                      np.array(['A6', 57, 58, 0, 0]),
                      np.array(['A7', 59, 28, 0, 0])]).reshape((8,5))
                      
        arrayTeamB = np.array([np.array(['GKB', 61, 62, 99, 100]), 
                  np.array(['B1', 63, 64, 0, 0]),
                  np.array(['B2', 65, 66, 0, 0]),
                  np.array(['B3', 67, 68, 0, 0]),
                  np.array(['B4', 69, 38, 0, 0]),
                  np.array(['B5', 71, 40, 0, 0]),
                  np.array(['B6', 73, 74, 0, 0]),
                  np.array(['B7', 75, 44, 0, 0])]).reshape((8,5))

        TeamB = DataFrame(arrayTeamB, columns=['ID', 'LL', 'RL', 'LA', 'RA'])
        TeamB.LL = TeamB.LL.astype(float)
        TeamB.RL = TeamB.RL.astype(float)
        TeamB.LA = TeamB.LA.astype(float)
        TeamB.RA = TeamB.RA.astype(float)
    
        TeamA = DataFrame(arrayTeamA, columns=['ID', 'LL', 'RL', 'LA', 'RA'])
        TeamA.LL = TeamA.LL.astype(float)
        TeamA.RL = TeamA.RL.astype(float)
        TeamA.LA = TeamA.LA.astype(float)
        TeamA.RA = TeamA.RA.astype(float)
        reader = pd.read_csv('../../Resources/SmallGame/full-game', 
                     names=['sid', 'ts', 'x', 'y', 'z', 'v', 'a', 'vx', 'vy', 'vz', 'ax', 'ay', 'az'], 
                     header=None, 
                     chunksize=1000000)
        garbage = reader.get_chunk(1549800)
        running_statistics_teamA, running_statistics_teamB = current_running_statistics(reader, TeamA, TeamB)
        print running_statistics_teamA
        print "=========================================================="
        print running_statistics_teamB
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCurrentRunningStat']
    unittest.main()