'''
Created on Mar 2, 2015

@author: kostadin
'''
import unittest
from pandas import DataFrame
from small_game.ball_possesion import extract_ball_possession
from small_game.ball_possesion import extract_passess
from small_game.ball_possesion import shots_on_goal
import pandas as pd
import numpy as np

class Test(unittest.TestCase):
    GOAL_AREA_1 = {'X_MIN': 22578.5, 'X_MAX': 29898.5, 'Y': 33941.0, 'Z_MAX': 2440.}
    GOAL_AREA_2 = {'X_MIN': 22560., 'X_MAX': 29880., 'Y': -33968.0, 'Z_MAX': 2440.}
    TIME = 1.5
    GRAVITY = 9.81 * 1e3

    def setUp(self):
        pass
        self.balls = [4, 8, 10, 12]
    
        arrayTeamA = np.array([np.array(['GKA', 13, 14, 97, 98]), 
                      np.array(['A1', 47, 16, 0, 0]),
                      np.array(['A2', 49, 88, 0, 0]),
                      np.array(['A3', 19, 52, 0, 0]),
                      np.array(['A4', 53, 54, 0, 0]),
                      np.array(['A5', 23, 24, 0, 0]),
                      np.array(['A6', 57, 58, 0, 0]),
                      np.array(['A7', 59, 28, 0, 0])]).reshape((8,5))

        self.TeamA = DataFrame(arrayTeamA, columns=['ID', 'LL', 'RL', 'LA', 'RA'])
        self.TeamA.LL = self.TeamA.LL.astype(float)
        self.TeamA.RL = self.TeamA.RL.astype(float)
        self.TeamA.LA = self.TeamA.LA.astype(float)
        self.TeamA.RA = self.TeamA.RA.astype(float)
        self.reader = pd.read_csv('../../Resources/SmallGame/full-game', 
                     names=['sid', 'ts', 'x', 'y', 'z', 'v', 'a', 'vx', 'vy', 'vz', 'ax', 'ay', 'az'], 
                     header=None, 
                     chunksize=1000000)
        garbage = self.reader.get_chunk(1549800)
        
        arrayTeamB = np.array([np.array(['GKB', 61, 62, 99, 100]), 
                  np.array(['B1', 63, 64, 0, 0]),
                  np.array(['B2', 65, 66, 0, 0]),
                  np.array(['B3', 67, 68, 0, 0]),
                  np.array(['B4', 69, 38, 0, 0]),
                  np.array(['B5', 71, 40, 0, 0]),
                  np.array(['B6', 73, 74, 0, 0]),
                  np.array(['B7', 75, 44, 0, 0])]).reshape((8,5))

        self.TeamB = DataFrame(arrayTeamB, columns=['ID', 'LL', 'RL', 'LA', 'RA'])
        self.TeamB.LL = self.TeamB.LL.astype(float)
        self.TeamB.RL = self.TeamB.RL.astype(float)
        self.TeamB.LA = self.TeamB.LA.astype(float)
        self.TeamB.RA = self.TeamB.RA.astype(float)
        

    def tearDown(self):
        pass
      

    def testBallPossession(self):
        pass
        self.ball_possession = extract_ball_possession(self.reader, self.TeamA, self.TeamB, self.balls)
        print self.ball_possession
        
    
#     def testExtractPassess(self):
#         pass
#         passess = extract_passess(self.ball_possession)
#         print passess
#         
#     
#     def testShootsOnGoal(self):
#         pass
#         shots = shots_on_goal(self.ball_possession)
#         print shots


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testBallPossession']
    unittest.main()