'''
Created on Jan 21, 2015

@author: kostadin
'''
import big_game.extract_action as extract_action
import big_game.extract_positions as extract_positions
from big_game.extract_action import score_attempts
import datetime as dt

if __name__ == '__main__':
    pass
    players_kaiser = ('ID5', 'ID6', 'ID7', 'ID8', 'ID9', 'ID10')
    players_hannover = ('ID16', 'ID17', 'ID18', 'ID19', 'ID20', 'ID21')
    score_attempts = extract_action.score_attempts()
    print score_attempts
    positions = extract_positions.extract()
#     print positions.ix[1, 1, 1]
    half1 = dt.datetime(2015, 1, 21, 15, 31, 59, 4)
    half2 = dt.datetime(2015, 1, 21, 16, 34, 7, 68)
    periods = (half1, half2)
#     event_time = extract_action.extract_event_window(score_attempts, "O_9", (half1, half2))
#     print extract_action.extract_trajectory(event_time[0], event_time[0]+250, positions.Team1, positions.Ball.Data, players_kaiser)
    trajectories = extract_action.extract_trajectories(score_attempts[score_attempts.team=='O_9'], positions.Team1, positions.Ball.Data, players_kaiser, periods, 10)
#     print len(trajectories)
    print trajectories[16]    