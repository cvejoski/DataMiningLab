'''
Created on Jan 21, 2015

@author: kostadin
'''

from xml.dom import minidom
import pandas as pd
from pandas import DataFrame
from helper.normalization import normalization

def score_attempts(file_path="../Resources/BigGame/Data/vistrack-actions-130375.xml"):
    DOMTree = minidom.parse(file_path)

    collection = DOMTree.documentElement
    
    score_attempts = collection.getElementsByTagName("action-soccer-score-attempt")
    column_names = ['id', 'period', 'minute', 'time_stamp', 'method', 
                    'team', 'player', 'second_player', 
                    'x1', 'y1', 'x2', 'y2', 'result', 'position']
    score_attempt_dic = {}
    for attempt in score_attempts:
        score_attempt_dic.setdefault(column_names[0], []).append(attempt.getAttribute("id"))
        score_attempt_dic.setdefault(column_names[4], []).append(attempt.getAttribute("score-attempt-method"))
        score_attempt_dic.setdefault(column_names[12], []).append(attempt.getAttribute("score-attempt-result"))
        score_attempt_dic.setdefault(column_names[13], []).append(attempt.getAttribute("score-attempt-position"))
        score_attempt_dic.setdefault(column_names[5], []).append(attempt.getAttribute("team-idref"))
        score_attempt_dic.setdefault(column_names[6], []).append(attempt.getAttribute("player-idref"))
        score_attempt_dic.setdefault(column_names[7], []).append(attempt.getAttribute("second-player-idref"))
        score_attempt_dic.setdefault(column_names[1], []).append(attempt.getAttribute("period-value"))
        score_attempt_dic.setdefault(column_names[2], []).append(attempt.getAttribute("minutes-elapsed"))
        score_attempt_dic.setdefault(column_names[3], []).append(attempt.getAttribute("timestamp"))
        score_attempt_dic.setdefault(column_names[8], []).append(attempt.getAttribute("x1"))
        score_attempt_dic.setdefault(column_names[9], []).append(attempt.getAttribute("y1"))
        score_attempt_dic.setdefault(column_names[10], []).append(attempt.getAttribute("x2"))
        score_attempt_dic.setdefault(column_names[11], []).append(attempt.getAttribute("y2"))
    
    
    score_attempt = DataFrame(score_attempt_dic, columns=column_names, dtype = float)
    
    #set empty coordinates to 0
    score_attempt.loc[[5, 9, 13, 19, 21, 23], [10, 11]] = 0
    
    #convert columns to appropriate data types
    score_attempt['time_stamp'] = pd.to_datetime(score_attempt.time_stamp)
    score_attempt['id'] = score_attempt['id'].astype(int)
    score_attempt['period'] = score_attempt['period'].astype(int)
    score_attempt['minute'] = score_attempt['minute'].astype(int)
    score_attempt['x2'] = score_attempt['x2'].astype(float)
    score_attempt['y2'] = score_attempt['y2'].astype(float)
    score_attempt.sort(columns="time_stamp")
    
    return score_attempt

def extract_trajectories(event_data, team_positions, ball_positions, players_tracked, periods, trajectory_size):
    time_stamps = __extract_event_timestamps(event_data, periods)
    trajectories = []
    for time_stamp in time_stamps:
        trajectories.append(__extract_trajectory(time_stamp[0], time_stamp[0]+25*trajectory_size, 
                                                team_positions.ix[time_stamp[1]], ball_positions.ix[time_stamp[1]], players_tracked))
    return trajectories

def __extract_trajectory(time_start, time_end, team, ball, players):
    trajectory = []
    it = team[time_start:time_end].iterrows()
    for index, row in it:
        snap_shot = []
        snap_shot.append(normalization(index[1], time_start, time_end-1))
        player_snap = []
        for p in players:
            if row[p].X == -10.:
                player_snap.append((0, 0))
            else:
                player_snap.append((row[p].X, row[p].Y))  
        
        snap_shot.extend([player_snap])
        snap_shot.append([(ball.ix[index].X, ball.ix[index].Y)])
#         print snap_shot
        trajectory.append(snap_shot)
    return trajectory

def __extract_event_timestamps(event_data, periods):    
    it_data = event_data.iterrows()
    result = []
    for index, row in it_data:
        if row.period == 1:
            result.append([int((row.time_stamp - periods[0]).seconds * 25), 1])
        else:
            result.append([int((row.time_stamp - periods[1]).seconds * 25), 2])
    return result
    