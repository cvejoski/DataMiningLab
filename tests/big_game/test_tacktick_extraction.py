'''
Created on Jan 25, 2015

@author: kostadin
'''
import unittest
import big_game.extract_action as extract_action
import big_game.extract_positions as extract_positions
import datetime as dt
import big_game.tacktick_extraction as te
import numpy as np
from helper.k_medoids import clustering

class Test(unittest.TestCase):
    

    def testName(self):
        players_kaiser = ('ID5', 'ID6', 'ID7', 'ID8', 'ID9', 'ID10')

        score_attempts = extract_action.score_attempts("../../Resources/BigGame/Data/vistrack-actions-130375.xml")     
        positions = extract_positions.extract("../../Resources/BigGame/Data/130375.pos")
   
        half1 = dt.datetime(2015, 1, 21, 15, 31, 59, 4)
        half2 = dt.datetime(2015, 1, 21, 16, 34, 7, 68)
        periods = (half1, half2)
        trajectories = extract_action.extract_trajectories(score_attempts[score_attempts.team=='O_9'], positions.Team1, positions.Ball.Data, players_kaiser, periods, 5)
#   
#         np.allclose(te.calculate_center(trajectories[15][0][1]), [0.1189333, 0.1331])
#         np.allclose(te.calculate_center(trajectories[16][249][1]), [-0.23005, 0.2739])
#         np.allclose(te.calculate_covariance(trajectories[15][0][1], te.calculate_center(trajectories[15][0][1]), 0.1, 0.1), [[ 0.31228175, -0.20937909], [-0.20937909,  0.5940079 ]])
        
#         print te.r_kernel(trajectories[0], trajectories[0])
#         print te.r_kernel(trajectories[1], trajectories[1])
#         print te.r_kernel(trajectories[2], trajectories[2])
#         print te.r_kernel(trajectories[3], trajectories[3])
#         print te.r_kernel(trajectories[4], trajectories[4])
#         print te.r_kernel(trajectories[5], trajectories[5])
#         print te.r_kernel(trajectories[6], trajectories[6])
#         print te.r_kernel(trajectories[7], trajectories[7])
#         print te.r_kernel(trajectories[8], trajectories[8])
#         print te.r_kernel(trajectories[9], trajectories[9])
#         print te.r_kernel(trajectories[10], trajectories[10])
#         print te.r_kernel(trajectories[11], trajectories[11])
#         print te.r_kernel(trajectories[12], trajectories[12])
#         print te.r_kernel(trajectories[13], trajectories[13])
#         print te.r_kernel(trajectories[14], trajectories[14])
#         print te.r_kernel(trajectories[15], trajectories[15])
#         print te.r_kernel(trajectories[16], trajectories[16])
        
        medoids, clusters = clustering(trajectories, 3)
        print medoids
        print clusters

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()